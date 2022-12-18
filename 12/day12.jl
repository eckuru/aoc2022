using Graphs
using Cairo
using GraphPlot
using Fontconfig
using Compose

struct HeightMap
    map::Matrix
end

function file_to_heightmap(path)
    file = open(path)
    lines = readlines(file)
    dimx = length(lines)
    dimy = length(lines[1])
    mat = zeros(Int, (dimx, dimy))
    for (i, l) in enumerate(lines)
        mat[i, :] = map(x -> char_to_height(x), collect(l))
    end
    HeightMap(mat)
end

function char_to_height(c)
    if c != 'E' && c != 'S'
        Int(c) - 97
    elseif c == 'E'
        26
    elseif c == 'S'
        -1
    end
end

function add_connections!(
    graph::Graphs.SimpleGraphs.AbstractGraph, srcnodes::Vector{CartesianIndex{2}},
    thisnode::Function, nextnode::Function, height::Int
)
    for i in srcnodes
        srci, srcj = thisnode(i[1], i[2])
        dsti, dstj = nextnode(i[1], i[2])
        srcnode = nodeid_from_indices(srci, srcj, height)
        dstnode = nodeid_from_indices(dsti, dstj, height)
        Graphs.add_edge!(graph, srcnode, dstnode)
    end
end

function parsegraph(height_map::HeightMap)
    graph = Graphs.SimpleGraphs.SimpleDiGraph(length(height_map.map))
    height, _ = size(height_map.map)

    distances_right = height_map.map[:, 1:end-1] - height_map.map[:, 2:end]
    distances_down = height_map.map[1:end-1, :] - height_map.map[2:end, :]

    # connect down
    add_connections!(
        graph,
        findall(distances_down .>= -1),
        (x, y) -> (x,y),
        (x, y) -> (x + 1, y),
        height
    )
    # connect up
    add_connections!(
        graph,
        findall((-1 .* distances_down) .>= -1),
        (x, y) -> (x + 1, y),
        (x, y) -> (x, y),
        height
    )

    # connect right
    add_connections!(
        graph,
        findall(distances_right .>= -1),
        (x, y) -> (x, y),
        (x, y) -> (x, y + 1),
        height
    )

    # connect left
    add_connections!(
        graph,
        findall((-1 * distances_right) .>= -1),
        (x, y) -> (x, y + 1),
        (x, y) -> (x, y),
        height
    )

    return graph
end

function nodeid_from_indices(row_id, col_id, col_len)
    return (col_id - 1) * col_len + row_id
end

function nodeid_from_indices(id_tuple, col_len)
    return nodeid_from_indices(id_tuple[1], id_tuple[2], col_len)
end

function nodeid_to_indices(node_id, col_len, row_len)
    i = ceil(node_id / col_len)
    j = ((node_id-1) % row_len) + 1
    return i, j
end

function main()
    path = "input.txt"
    hmap = file_to_heightmap(path)
    graph = parsegraph(hmap)
    width, height = size(hmap.map)
    plot_graph(graph, width, height)
    dstnode = nodeid_from_indices(findfirst(hmap.map .== 26), size(hmap.map)[1])
    return graph, hmap, dstnode
end

function part1()
    graph, hmap, dst = main()
    src = nodeid_from_indices(findfirst(hmap.map .== -1), size(hmap.map)[1])
    return Graphs.dijkstra_shortest_paths(graph, src).dists[dst]
end

function part2()
    graph, hmap, dst = main()
    srcnodes = [nodeid_from_indices(i, size(hmap.map)[1]) for i in findall(hmap.map .<= 0)]
    shortest_paths = map(src -> Graphs.dijkstra_shortest_paths(graph, src).dists[dst], srcnodes)
    return minimum(shortest_paths)
end


function mylayout(graph, width, height)
    nodecount = size(graph)[1]
    loc_x = Int.(ceil.(collect(1:nodecount) ./ width))
    loc_y = repeat(collect(1:width), height)
    return loc_x, loc_y
end


function plot_graph(graph, width, height)
    draw(PNG("test.png", 16cm, 16cm), gplot(graph, layout=x->mylayout(x, width, height), nodelabel=1:length(vertices(graph))))
end # module



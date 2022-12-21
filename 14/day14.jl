function main(path)
    cavemap, ymin = parse_input(path)
    cavemap, count = add_sand!(cavemap, ymin)
    return cavemap, count
end

function parse_input(path)
    file = open(path)
    lines = readlines(file)
    points = parse_line.(lines)
    allpoints = append!(points...)
    # inverted indexing in the input
    xmax = maximum([i[2] for i in allpoints])
    ymin = minimum([i[1] for i in allpoints]) - 1
    ymax = maximum([i[1] for i in allpoints])
    cavemap = zeros(Int8, xmax, ymax-ymin)

    map(x -> fill_cavemap!(cavemap, x, ymin), points)
    return cavemap, ymin
end

function parse_line(line)
    points = split.(split(line, " -> "), ",")
    return map(x -> eval.(Meta.parse.(x)), points)
end

function fill_cavemap!(cavemap, points_in_line, ymin)
    for i in 1:length(points_in_line)-1
        add_line!(cavemap, points_in_line[i], points_in_line[i+1], ymin)
    end
end

function add_line!(cavemap, point1, point2, ymin)
    y1, x1 = point1
    y2, x2 = point2
    if x1 == x2
        cavemap[x1, minimum([y1, y2])-ymin:maximum([y1, y2])-ymin] .= 1
    elseif y1 == y2
        cavemap[minimum([x1, x2]):maximum([x1, x2]), y1-ymin] .= 1
    end
end

function add_sand!(cavemap, ymin)
    sandpoint = [1, 500 - ymin]
    print(sandpoint)
    count = -1
    landing = true
    while landing
        landing = falling_sand!(cavemap, sandpoint)
        count += 1
    end
    return cavemap, count
end

function falling_sand!(cavemap, sandpoint)
    sandx, sandy = sandpoint
    firstblock = findfirst(cavemap[sandx:end,sandy] .> 0)
    if isnothing(firstblock)
        return false
    else
        if sandy > 1
            if  cavemap[sandx+firstblock-1, sandy-1] == 0
                return falling_sand!(cavemap, (sandx + firstblock - 1, sandy - 1))
            end
        else
            return false
        end
        if sandy < size(cavemap)[2]
            if cavemap[sandx+firstblock-1, sandy+1] == 0
                return falling_sand!(cavemap, (sandx + firstblock - 1, sandy + 1))
            end
        else
            return false
        end
        cavemap[sandx+firstblock-2, sandy] = 2
        return true
    end
end

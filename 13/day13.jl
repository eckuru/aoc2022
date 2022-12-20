

function parse_input(path)
    file = open(path)
    lines = eval.(Meta.parse.(readlines(file)))
    groups = reshape(lines, 2, Int(length(lines) / 2))

end

function compare_groups(groups)
    comparison_results = zeros(size(groups)[2])
    for (i, group) in enumerate(eachcol(groups))
        comparison = compare_groups(group[1], group[2])
        if isnothing(comparison)
            if length(group[1]) < length(group[2])
                comparison_results[i] = i
            end
            continue
        elseif comparison
            comparison_results[i] = i
        end

    end
    return comparison_results
end

function compare_groups(left, right, ordered=nothing)
    for (i, j) in zip(left, right)
        comparison = compare(i, j, ordered)
        if comparison == -1 || isnothing(comparison)
            continue
        else
            ordered = comparison
            break
        end
    end

    if isnothing(ordered)
        return length(left) <= length(right) ? true : false
    else
        return ordered
    end
end



function compare(int1::Int64, int2::Int64, ordered=nothing)
    return int1 == int2 ? -1 : int1 <= int2
end

function compare(list1::Vector, list2::Vector, ordered=nothing)
    return compare_groups(list1, list2, ordered)
end


function compare(list::Vector, int::Int64, ordered=nothing)

    return compare_groups(list, [int], ordered)
end


function compare(int::Int64, list::Vector, ordered=nothing)
    return compare_groups([int], list, ordered)
end

function part1(groups)
    comparison = compare_groups(groups)
    return sum(comparison)
end

function part2(groups)
    index2 = sum(map(x -> compare_groups(x, [[2]]), groups))
    index6 = sum(map(x -> compare_groups(x, [[6]]), groups)) + 1
    return index2 * index6
end

function main()
    path = "input.txt"
    groups = parse_input(path)
    println("Part 1: ", part1(groups))
    println("Part 2: ", part2(groups))
end

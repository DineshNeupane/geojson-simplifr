from line import Line


def simplifyGeometry(points, tolerance):
    dmax = 0
    index = 0
    results = []
    for i in range(1, len(points) - 1):
        d = Line(points[0], points[len(points) - 1]).perpendiculardistance(points[i])
        if d > dmax:
            index = i
            dmax = d
    if dmax > tolerance:
        results_one = simplifyGeometry(points[0:index], tolerance)
        results_two = simplifyGeometry(points[index:len(points)], tolerance)
        results = results_one + results_two

    elif len(points) > 1:
        results = [points[0], points[len(points) - 1]]
    else:
        results = [points[0]]

    return results

##########################################################################################
#       A Graham Scan Algorithm.
#       Given a 'gift' (list of 2D/3D points) return a subset of gift 
#       containing points that, when connected, wrap all the points 
#       in the gift as tightly as possible.
#       
#       Source: https://www.algorithm-archive.org/contents/graham_scan/graham_scan.html
##########################################################################################

# Code adopted directly from the source above. Additional comments added by me.

from math import atan2

# Given three points (x,y), return whether the connection p1->p2->p3 is counter clockwise. 
def counter_clockwise(p1, p2, p3):
    """Is the turn counter-clockwise?"""
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

def polar_angle(ref, point):
    """Find the polar angle of a point relative to a reference point"""
    return atan2(point[1] - ref[1], point[0] - ref[0])

# Given a 'gift' (list of points (x,y)), return all the points that make up a convex polygon such that,
# when all the polygon's points are connected, the polygon's area is as small as possible but inscribes all
# other points in the gift inside.
def graham_scan(gift):
    gift = list(set(gift))  # Remove duplicate points
    start = min(gift, key=lambda p: (p[1], p[0]))  # Start at the point with the smallest x/y.
    gift.remove(start)

    s = sorted(gift, key=lambda point: polar_angle(start, point)) # Sort the gift based on 
    hull = [start, s[0], s[1]]

    # Remove points from hull that make the hull concave
    for pt in s[2:]:
        while not counter_clockwise(hull[-2], hull[-1], pt):
            del hull[-1] # if the three points form a clockwise rotation, delete the middle point (because the middle point causes the concave-ness).
        hull.append(pt)  

    return hull
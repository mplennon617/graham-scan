##########################################################################################
#       A Graham Scan Algorithm.
#       Given a 'gift' (list of 2D/3D points) return a subset of gift 
#       containing points that, when connected, wrap all the points 
#       in the gift as tightly as possible.
#       
#       Source: https://www.algorithm-archive.org/contents/graham_scan/graham_scan.html
##########################################################################################

# Code adopted directly from the source above. Comments added by me.
from math import atan2

# Given three points {s_k-1, s_k, s_k+1}, return whether the connection s_k-1->s_k->s_k+1 counter clockwise. 
def counter_clockwise(p1, p2, p3):
    """Is the turn counter-clockwise?"""
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

# Given a point s_k relative to an origin point P, find the polar angle from P to s_k.
def polar_angle(ref, point):
    """Find the polar angle of a point relative to a reference point"""
    return atan2(point[1] - ref[1], point[0] - ref[0])

# Given a 'gift' S (list of points (x,y)), return all the points that construct a convex hull for the gift.
# The convex hull will be a subset of the gift.
def graham_scan(gift):
    gift = list(set(gift))  # Remove duplicate points
    start = min(gift, key=lambda p: (p[1], p[0]))  # In this specific implementation, we start with the bottom point as P.
    gift.remove(start)

    s = sorted(gift, key=lambda point: polar_angle(start, point)) # Sort the gift based on increasing polar angle about the starting point.
    hull = [start, s[0], s[1]]

    # Remove points from hull that make the hull concave
    # NOTE: In this implementation, we treat 'pt' as s_k+1.
    for pt in s[2:]:
        while not counter_clockwise(hull[-2], hull[-1], pt):
            del hull[-1] # if the three points form a clockwise rotation, delete the middle point from the hull (s_k).
        hull.append(pt) # Append pt (s_k+1) to the hull. It will be checked as s_k in the next iteration of this loop and may be deleted.

    return hull
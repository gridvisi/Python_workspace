
import colour
XYZ = [0.07049534, 0.10080000, 0.09558313]
A = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['A']
D65 = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D65']
print(colour.chromatic_adaptation(XYZ, colour.xy_to_XYZ(A), colour.xy_to_XYZ(D65)))
#array([ 0.08398225,  0.11413379,  0.28629643])
print(sorted(colour.CHROMATIC_ADAPTATION_METHODS.keys()))


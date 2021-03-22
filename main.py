# Search methods

import search

p1 = search.GPSProblem('A', 'B', search.romania)
p2 = search.GPSProblem('O', 'N', search.romania)
p3 = search.GPSProblem('L', 'E', search.romania)
p4 = search.GPSProblem('S', 'U', search.romania)
p5 = search.GPSProblem('P', 'L', search.romania)

print(search.ramificacion_y_acotacion(p1).path())
print(search.ramificacion_y_acotacion_subestimacion(p1).path())
print("")
print(search.ramificacion_y_acotacion(p2).path())
print(search.ramificacion_y_acotacion_subestimacion(p2).path())
print("")
print(search.ramificacion_y_acotacion(p3).path())
print(search.ramificacion_y_acotacion_subestimacion(p3).path())
print("")
print(search.ramificacion_y_acotacion(p4).path())
print(search.ramificacion_y_acotacion_subestimacion(p4).path())
print("")
print(search.ramificacion_y_acotacion(p5).path())
print(search.ramificacion_y_acotacion_subestimacion(p5).path())



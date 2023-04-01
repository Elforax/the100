import cadquery as cq 
from cadquery import exporters

height = 60.0
width = 80.0
thickness = 10.0


# make the base
result = (cq.Workplane("XY")
            .box(height, width, thickness)
            .Workplane(">Z")
            .box(height/2, width/2, thickness)
            .edges("|Z")
            .fillet(2.0)
            )



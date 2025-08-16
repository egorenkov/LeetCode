class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        
        # Берем первые две точки для определения уравнения прямой
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Проверяем вертикальную линию (x = const)
        if x0 == x1:
            return all(p[0] == x0 for p in coordinates)
        
        # Проверяем горизонтальную линию (y = const)
        if y0 == y1:
            return all(p[1] == y0 for p in coordinates)
        
        # Для наклонных линий используем уравнение (x - x0)(y1 - y0) = (y - y0)(x1 - x0)
        dx = x1 - x0
        dy = y1 - y0
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * dy != (y - y0) * dx:
                return False
        
        return True

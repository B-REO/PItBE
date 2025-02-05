def read_xyz(filename):
    geometry = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    for line in lines[2:]:  
        parts = line.split()
        atom = parts[0]  
        coordinates = list(map(float, parts[1:4]))  
        geometry.append([atom, coordinates])
    
    return geometry

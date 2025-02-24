l, c = [int(i) for i in input().split(" ")]

photo = []

for _ in range(l) : 

    pixels = input().split(" ")
    photo.append(pixels)

def check_color(l, photo) :

    for pixels in photo : 

        if "C" in pixels or "M" in pixels or "Y" in pixels :
            return "#Color"
        
    return "#Black&White"

print(check_color(l, photo))
print("\nWelcome, please fill out the info")

HEIGHT = input("Enter Height: ")
WIDTH = input("Enter Width: ")
AmountOfLines = input("Enter Amount of Coordinates: ")

HEIGHTSPACE = int(HEIGHT) / int(AmountOfLines)
WIDTHSPACE = int(WIDTH) / int(AmountOfLines)

heightSpace = int(HEIGHT) / int(AmountOfLines)
widthSpace = int(WIDTH) / int(AmountOfLines)
fontSizeX = int(WIDTH) / 25
fontSizeY = int(HEIGHT) / 25



with open('test.svg', 'w') as f:
    f.write(f'<svg style="border:  green solid;" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">')
    for i in range(int(AmountOfLines)):
        f.write(f'<path stroke="green" stroke-width=".3" d="M{heightSpace} 0 V{HEIGHT} "/>')
        f.write(f'<path stroke="green" stroke-width=".3" d="M0 {widthSpace} H{WIDTH} "/>')

        f.write(f'<text font-size="{fontSizeX}" x="{widthSpace}" y="1">{round(widthSpace)}</text>')
        f.write(f'<text font-size="{fontSizeY}" y="{heightSpace}" x="1">{round(heightSpace)}</text>')

        heightSpace += HEIGHTSPACE
        widthSpace += WIDTHSPACE

    f.write("\n\n<svg/>")
    f.close()

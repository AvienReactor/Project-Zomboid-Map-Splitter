import cv2


def SplitMap(in_path, out_path, type, col, row):
    col = int(col)
    row = int(row)
    tmptype = "def"

    match str(type):
        case "N":
            tmptype = "";
        case "o":
            tmptype = "_veg";
        case "r":
            tmptype = "_zs"

    image = cv2.imread(in_path)
    if image is not None:
        (h, w) = image.shape[:2]
        centerX, centerY = (w // row), (h // col)
        for rows in range(col):
            for columns in range(row):
                middleRight = image[centerY * rows:centerY * (rows + 1), centerX * columns:centerX * (columns+1)]
                tmppath = str(out_path).replace("/","\\")
                tmpjoin = "\Tile_{},{}{}.png".format(columns, rows, tmptype)
                tmppath = tmppath + tmpjoin
                cv2.imwrite(tmppath, middleRight)
    else:
        print('variable is None')
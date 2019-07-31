
import sys
from .models import Game

def boardHTML(board):
    output = "" # board in HTML 
    rawBoard = "" # string representation of board
    evenodd = 0 # upper left corner is white square

    #print('BOARD:' + ''.join(map(str,board)), file=sys.stderr)
    output = ""

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    for cols in 'abcdefgh':
        output = output + "<div class=\"square-top\" >" + cols + "</div>"

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    output = output + "<br>"

    for rc, row in enumerate(board): # ranks
        rank = (8-rc)
        output = output + "<div class=\"square-side\" >" + str(rank) + "</div>"
        for cc, col in enumerate(row): # files
            #print("Col = " + str(col), file=sys.stderr)
            if evenodd % 2 == 0:
                output = output + "<div class=\"squarew\" "
            else:
                output = output + "<div class=\"squareb\" "

            coords = str(chr(cc+1+96)) + str(rank)
            i = col

            if col == '.':
                output = output + "onclick=\"addPiece('" + coords + "')\"></div>"
            else:
                # if there's a peice here get the image
                if i.islower(): # is piece black?
                    code = "b" + i.lower()
                else:
                    code = "w" + i.lower()
                output = output + "onclick=\"addPiece('" + coords + "')\" style=\"background-image: url('/static/images/p/" + code + ".png')\"></div>"
            
            evenodd = evenodd + 1
            rawBoard = rawBoard + i
        # start the next row as a different color
        output = output + "<div class=\"square-side\" >" + str(rank) + "</div>"
        evenodd = evenodd + 1
        output = output + "<br>\n"

        # <div class="square1" onclick="addPiece('h1');"></div>

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    for cols in 'abcdefgh':
        output = output + "<div class=\"square-top\" >" + cols + "</div>"

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"
    output = output + "<br><div id=\"rawboard\">" + rawBoard + "</div>"
    #print(output, file=sys.stderr)
    return output

def thumbnailBoardHTML(board):
    output = "" # board in HTML 
    rawBoard = "" # string representation of board
    evenodd = 0 # upper left corner is white square
    output = ""

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    for cols in 'abcdefgh':
        output = output + "<div class=\"square-top\" >" + cols + "</div>"

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    output = output + "<br>"

    for rc, row in enumerate(board): # ranks
        rank = (8-rc)
        output = output + "<div class=\"square-side\" >" + str(rank) + "</div>"
        for cc, col in enumerate(row): # files
            #print("Col = " + str(col), file=sys.stderr)
            if evenodd % 2 == 0:
                output = output + "<div class=\"squarew\" "
            else:
                output = output + "<div class=\"squareb\" "

            coords = str(chr(cc+1+96)) + str(rank)
            i = col

            if col == '.':
                output = output + "onclick=\"addPiece('" + coords + "')\"></div>"
            else:
                # if there's a peice here get the image
                if i.islower(): # is piece black?
                    code = "b" + i.lower()
                else:
                    code = "w" + i.lower()
                output = output + "onclick=\"addPiece('" + coords + "')\" style=\"background-image: url('/static/images/p/" + code + ".png')\"></div>"
            
            evenodd = evenodd + 1
            rawBoard = rawBoard + i
        # start the next row as a different color
        output = output + "<div class=\"square-side\" >" + str(rank) + "</div>"
        evenodd = evenodd + 1
        output = output + "<br>\n"

        # <div class="square1" onclick="addPiece('h1');"></div>

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"

    for cols in 'abcdefgh':
        output = output + "<div class=\"square-top\" >" + cols + "</div>"

    output = output + "<div class=\"square-corner\" >&nbsp;</div>"
    output = output + "<br><div id=\"rawboard\">" + rawBoard + "</div>"
    #print(output, file=sys.stderr)
    return output

def printBoard(board):
    print("  a b c d e f g h")
    for rc, row in enumerate(board):
        print(str(rc), end='')
        for col in row:
            print(' ' + col, end='')
        print(' ' + str(rc), end='')
        print('')
    print("  a b c d e f g h")


def parseInputString(s):
    command = ''
    for c in s:
        if c.isdigit() or c.isalpha():
            command = command + c
    if len(command) != 4:
        return 'ERR - invalid length'
        # some other command
    else:
        if command[0].isalpha() and command[2].isalpha():
            if command[1].isdigit() and command[3].isdigit():
                return command			
            else:
                return    'ERR - invalid pattern'
        else:
            return 'ERR - invalid pattern'

#
# Read/write board to/from database
#

def readBoardDB(game_id):
    g = Game.objects.get(pk=game_id)
    board = g.board

    boardList = []
    colList = []
    # split in 8 rows of 8
    for row in range(0,8):
        colList = []
        for col in range(0,8):
            colList.append(board[(row * 8) + col])
        boardList.append(colList)
    return boardList

def writeBoardDB(game_id, board):
    s = ""
    for row in board:
        for col in row:
            s = s + col
    g = Game.objects.get(pk=game_id)
    g.board = s
    g.save()            
    return

#
# Read/write board to/from text files
#

def readBoardFile(filename):
    input = open("games/" + filename, 'r')
    print("Reading board from file " + filename, file=sys.stderr)
    board = input.read()
    board = board.rstrip()
    boardList = []
    colList = []

    # split in 8 rows of 8
    for row in range(0,8):
        colList = []
        for col in range(0,8):
            colList.append(board[(row * 8) + col])
        boardList.append(colList)
        #print(colList, file=sys.stderr)
    input.close()
    return boardList
    # return 'NONE' if error

def writeBoardFile(filename, board):
    output = open("games/" + filename, 'w')
    print("Writing board to file " + filename, file=sys.stderr)
    s = ""
    for row in board:
        for col in row:
            s = s + col
    output.write(s)
    output.close()
    return

def isPlayersTurn(player, game):
    if game.turn_color() == 'black':
        if player.id != game.black.id:
            return False
    elif game.turn_color() == 'white':
        if  player.id != game.white.id:
            return False
    return True

# find position of king
# start one corner of board
# for each piece
# is it color x
# is king position a valid move for this piece?
# next piece
def checkForCheck(color, board):
    # return true if color 'is in check'
    if color != 'black' and color != 'white':
        return('info', 'must pass black or white to checkForCheck')
    # find the king
    for col in 'abcdefgh':
        for row in range(1, 9):
            x = toArrayCoords(toNumCoords(col))
            y = rankToArrayCoords(row)
            p = board[y][x]
            if color == 'black':
                if p == 'k':
                    # print('found the black king at ' + col + str(row))
                    king_x = col
                    king_y = row
            if color == 'white':
                if p == 'K':
                    # print('found the white king at ' + col + str(row))
                    king_x = col
                    king_y = row

    # brute-force check if every piece is putting the king in check
    for col in 'abcdefgh':
        for row in range(1, 9):
            x = toArrayCoords(toNumCoords(col))
            y = rankToArrayCoords(row)
            p = board[y][x]
            if color == 'white':
                if p.islower(): # is this a black piece?
                    # is it a valid move from here to the king?
                    result = processMove(col+str(row)+king_x+str(king_y), board)
                    # print('Checking if the piece ' + p + ' at ' + col + str(row) + " puts white in check", file=sys.stderr)
                    # print(result)
                    if len(result) > 2: # did it return a whole board?
                        print('WHITE is in check by piece at ' + col + str(row), file=sys.stderr)
                        return True
            else:
                if p.isupper(): # is this a white piece?
                    # is it a valid move from here to the king?
                    result = processMove(col+str(row)+king_x+str(king_y), board)
                    # print('Checking if the piece ' + p + ' at ' + col + str(row) + " puts black in check", file=sys.stderr)
                    # print(result)
                    if len(result) > 2: # did it return a whole board?
                        print('BLACK is in check by piece at ' + col + str(row), file=sys.stderr)
                        return True
    return False

def processMove(movestring, board):
    # convert c2c3 to 2,1  2, 2
    x1 = toArrayCoords(toNumCoords(movestring[0]))
    x2 = toArrayCoords(toNumCoords(movestring[2]))
    y1 = rankToArrayCoords(int(movestring[1]))
    y2 = rankToArrayCoords(int(movestring[3]))

    p = board[y1][x1]
    # you can't move a blank piece
    if p == '.':
        return ('invalid', 'blank piece cannot be moved')

    # make sure both coords are different squares
    if x1 == x2 and y1 == y2:
        return ('invalid', 'cannot move to same square')
    # are coords on the board? not sure how this would happen...
    if not isMoveOnBoard(x1,x2,y1,y2):
        return ('invalid', 'one or more squares not on board')

    # see who is moving, white or black
    if p.isupper():
        piececolor = 'white'
    else:
        piececolor = 'black'
    #print('Piece is ' + piececolor, file=sys.stderr)
    
    p = p.lower()
    # check if move is valid, according to which piece it is

    # PAWNS
    if p == 'p':
        # Pawn: Forward 1, diagonal 1, or forward 2 if first move
        if y2 < y1: # are we moving 'up' the board
            if piececolor == 'black':
                return ('invalid', 'wrong direction for black pawn')
        else: # we are moving 'down' the board'
            if piececolor == 'white':
                return ('invalid', 'wrong direction for white pawn')

        if abs(y1 - y2) > 2:
            return ('invalid', 'pawn can only move 1 or 2 squares')

        if piececolor == 'white':
            if abs(y1 - y2) == 2: # moving 2 squares
                if y1 == 6: # first move of pawn, 2nd row, arrays start at 0
                    if x1 == x2: # make sure it's not diagonal
                        if board[y2][x2] == '.' and board[y1-1][x2]: # if both squares ahead are empty, allow move
                            board[y2][x2] = board[y1][x1]
                            board[y1][x1] = '.'
                            return board
                        else:
                            return ('invalid', 'pawn cannot move to occupied square')
                    else:
                        return ('invalid', 'pawn can only move straight on first move')
                else:
                    return ('invalid', 'pawn cannot move two squares except on first move')
            else: # moving 1 square
                if abs(x1 - x2) > 1:
                    return ('invalid', 'pawn cannot move sideways more than 1 square')
                elif x1 == x2: # moving 1 forward
                    if board[y2][x2] == '.': # if blank, allow move
                        board[y2][x2] = board[y1][x1]
                        board[y1][x1] = '.'
                        return board
                    else:
                        return ('invalid', 'pawn cannot move to occupied square')
                else: # moving diag
                    if board[y2][x2].islower(): # if opposite color
                        board[y2][x2] = board[y1][x1]
                        board[y1][x1] = '.'
                        return board
                    else:
                        return ('invalid', 'pawn cannot capture own piece')
        else: # moving black
            if abs(y1 - y2) == 2: # moving 2 squares
                if y1 == 1: # first move of pawn, 7th row, arrays start at 0
                    if x1 == x2: # make sure it's not diagonal
                        if board[y2][x2] == '.' and board[y1+1][x2]: # if both squares ahead are empty, allow move
                            board[y2][x2] = board[y1][x1]
                            board[y1][x1] = '.'
                            return board
                        else:
                            return ('invalid', 'pawn cannot move to occupied square')
                    else:
                        return ('invalid', 'pawn can only move straight on first move')
                else:
                    return ('invalid', 'pawn cannot move two squares except on first move')
            else: # moving 1 square
                if abs(x1 - x2) > 1:
                    return ('invalid', 'pawn cannot move sideways more than 1 square')
                elif x1 == x2: # moving 1 forward
                    if board[y2][x2] == '.': # if blank, allow move
                        board[y2][x2] = board[y1][x1]
                        board[y1][x1] = '.'
                        return board
                    else:
                        return ('invalid', 'pawn cannot move to occupied square')
                else: # moving diag
                    if board[y2][x2].isupper(): # if opposite color
                        board[y2][x2] = board[y1][x1]
                        board[y1][x1] = '.'
                        return board
                    else:
                        return ('invalid', 'pawn cannot capture own piece')

    # ROOKS
    if p == 'r':
        return attemptHorizMove(x1, y1, x2, y2, piececolor, board)

    # BISHOPS
    if p == 'b':
        return attemptDiagMove(x1, y1, x2, y2, piececolor, board)

    # QUEENS
    if p == 'q':
        result = attemptDiagMove(x1, y1, x2, y2, piececolor, board)
        if len(result) == 2:
            result = attemptHorizMove(x1, y1, x2, y2, piececolor, board)
        else:
            return result

        if len(result) == 2:
            return('info', 'probably not a legal move')
        else:
            return result

    # HORSEYS
    if p == 'n':
        move = ''
        if abs(x1-x2) == 2:
            if abs(y1-y2) == 1:
                move = 'legal'
        if abs(x1-x2) == 1:
            if abs(y1-y2) == 2:
                move = 'legal'
        if move == 'legal':
            return attemptMove(x1, y1, x2, y2, piececolor, board)

        return('info', 'probably not a legal move')

    # KING
    if p == 'k':
        if abs(x1-x2) <= 1: # only allow piece to move one square
            if abs(y1-y2) <= 1:
                return attemptMove(x1, y1, x2, y2, piececolor, board)
        return('info', 'probably not a legal move')

    # check for check/mate
    
    return('info', 'made it all the way through the piece loop...probably not good')

def attemptDiagMove(x1, y1, x2, y2, piececolor, board):
    if (abs(x1-x2) == abs(y1-y2)): # moved diagonal
        if abs(x1-x2) > 1: # is it more than one space away?
            # figure out the direction
            if (x1-x2) < 0: # going right
                x_step = 1
            else:           # going left
                x_step = -1
            if (y1-y2) < 0: # going up
                y_step = 1
            else:
                y_step = -1

            x_check = x1 + x_step
            y_check = y1 + y_step
            #print("x_step = " + str(x_step) + " y step = " +  str(y_step))

            while x_check != x2:
                #print("Checking " + str(x_check) + "," + str(y_check), file=sys.stderr)
                if board[y_check][x_check] != '.':
                    return('invalid', 'path is blocked')
                x_check += x_step
                y_check += y_step

    else:
        return('info', 'probably not a legal move')
    # move if not taken
    return attemptMove(x1, y1, x2, y2, piececolor, board)

def attemptHorizMove(x1, y1, x2, y2, piececolor, board):
    if (abs(x1-x2) == 0) ^ (abs(y1-y2) == 0): # moved horizontal
        if abs(x1-x2) == 0: # moved up/down
            if y1 < y2: # up
                if y2 - y1 > 1: # more than one space away? test squares in between
                    for test_y in range(y1+1, y2):
                      if board[test_y][x1] != '.':
                        return ('invalid', 'path is blocked (up)')
            else: # down
                if y1 - y2 > 1: # more than one space away? test squares in between
                    for test_y in range(y2+1, y1):
                      if board[test_y][x1] != '.':
                        return ('invalid', 'path is blocked (down)')
        else: # moved left/right
            if x1 < x2: # right
                if x2 - x1 > 1: # more than one space away? test squares in between
                    for test_x in range(x1+1, x2):
                      if board[y1][test_x] != '.':
                        return ('invalid', 'path is blocked (right)')
            else: # left
                if x1 - x2 > 1: # more than one space away? test squares in between
                    for test_x in range(x2+1, x1):
                      if board[y1][test_x] != '.':
                        return ('invalid', 'path is blocked (left)')
    elif (abs(x1-x2) == abs(y1-y2)): # moved diagonal
        return('info', 'rook cannot move diagonal')
    else:
        return('info', 'rook can only move vertical or horizontal')

    return attemptMove(x1, y1, x2, y2, piececolor, board)

def attemptMove(x1, y1, x2, y2, piececolor, board):
    if board[y2][x2] == '.': # empty space, we can move there
        board[y2][x2] = board[y1][x1]
        board[y1][x1] = '.'
        return board
    else:
        if piececolor == 'white':
            if board[y2][x2].islower(): # if opposite color
                board[y2][x2] = board[y1][x1]
                board[y1][x1] = '.'
                return board
            else:
                return('invalid', 'cannot capture own piece')
        else:
            if board[y2][x2].isupper(): # if opposite color
                board[y2][x2] = board[y1][x1]
                board[y1][x1] = '.'
                return board
            else:
                return('invalid', 'cannot capture own piece')

# convert a, b, c .. to 1, 2 3 ..
def toNumCoords(c):
    return ord(c.lower()) - 96 # ascii 'a' is 97

# convert 1, 2, 3 .. to 0, 1, 2 ..
def toArrayCoords(i):
    return i-1

# convert 8, 7, 6 .. to 0, 1, 2 ..
def rankToArrayCoords(i):
    return 8-i

def isMoveOnBoard(x1,x2,y1,y2):
    if x1 > 7 or x1 < 0:
        return False
    elif  x2 > 7 or x2 < 0:
        return False
    elif  y1 > 7 or y1 < 0:
        return False
    elif  y2 > 7 or y2 < 0:
        return False
    else:
        return True

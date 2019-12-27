import threading, queue
from intcode_machine import IntcodeMachine


input_code = [1,380,379,385,1008,2875,924596,381,1005,381,12,99,109,2876,1101,0,0,383,1102,0,1,382,21001,382,0,1,21002,383,1,2,21102,1,37,0,1106,0,578,4,382,4,383,204,1,1001,382,1,382,1007,382,43,381,1005,381,22,1001,383,1,383,1007,383,26,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1105,1,119,1007,392,41,381,1006,381,161,1102,1,1,384,21001,392,0,1,21102,1,24,2,21101,0,0,3,21102,138,1,0,1106,0,549,1,392,384,392,21001,392,0,1,21102,24,1,2,21102,3,1,3,21102,161,1,0,1105,1,549,1102,1,0,384,20001,388,390,1,20101,0,389,2,21101,0,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20102,1,389,2,21102,205,1,0,1105,1,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21102,228,1,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,20101,0,388,1,20001,389,391,2,21102,1,253,0,1106,0,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,0,304,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1101,0,1,384,1005,384,161,20101,0,388,1,21002,389,1,2,21102,1,0,3,21102,1,338,0,1105,1,549,1,388,390,388,1,389,391,389,21002,388,1,1,21002,389,1,2,21102,1,4,3,21102,365,1,0,1105,1,549,1007,389,25,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,452,19,21,1,1,21,109,3,21201,-2,0,1,21202,-1,1,2,21101,0,0,3,21102,414,1,0,1105,1,549,22101,0,-2,1,22102,1,-1,2,21101,429,0,0,1106,0,601,1201,1,0,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21201,-3,0,-7,109,-8,2106,0,0,109,4,1202,-2,43,566,201,-3,566,566,101,639,566,566,2102,1,-1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,43,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2105,1,0,109,3,22102,26,-2,1,22201,1,-1,1,21101,0,563,2,21102,904,1,3,21102,1118,1,4,21101,0,630,0,1105,1,456,21201,1,1757,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,2,2,2,2,0,0,0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,0,2,2,2,2,2,2,0,2,0,0,1,1,0,0,2,2,0,2,2,0,2,2,0,2,0,0,0,0,0,2,2,2,2,0,2,0,0,2,2,0,0,2,2,2,0,2,2,0,2,2,0,2,0,1,1,0,2,2,2,2,2,2,2,2,0,2,0,0,0,0,2,2,0,2,0,0,0,0,2,2,2,2,2,0,2,2,2,2,0,0,2,0,0,0,2,0,1,1,0,0,0,0,2,2,2,0,2,0,2,2,0,2,2,0,0,2,0,2,2,2,0,0,0,2,2,2,0,2,0,2,2,2,0,0,0,2,0,0,0,1,1,0,2,2,2,0,2,2,0,2,2,0,0,0,2,2,0,2,2,2,0,2,0,0,0,0,2,2,0,2,2,2,0,2,2,2,0,2,0,2,2,0,1,1,0,2,2,0,2,2,0,2,2,2,0,0,0,0,0,0,2,0,2,2,2,2,2,2,0,0,2,2,2,2,2,0,2,2,2,2,0,0,0,2,0,1,1,0,0,2,2,0,0,2,0,2,2,2,2,0,0,2,2,2,2,0,2,0,2,2,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,0,2,0,1,1,0,2,0,2,2,0,2,2,0,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,2,2,2,0,1,1,0,2,0,2,0,0,0,2,2,0,2,0,2,2,2,2,2,0,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,0,0,2,0,1,1,0,2,2,0,0,2,2,2,2,2,2,0,2,0,0,0,2,2,2,2,2,2,2,0,2,2,2,0,0,2,0,0,0,2,2,2,0,0,0,0,0,1,1,0,2,2,0,2,2,2,2,0,0,0,2,2,2,2,2,2,0,2,2,0,2,2,0,2,2,0,2,2,0,0,2,0,2,2,2,2,2,0,2,0,1,1,0,0,0,2,2,2,2,2,2,2,2,2,2,0,2,0,2,2,2,0,0,0,2,2,2,0,0,2,2,2,0,2,0,0,0,2,0,2,0,2,0,1,1,0,2,0,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,2,2,2,0,0,0,0,2,2,0,2,2,0,2,2,2,0,2,2,2,2,2,0,1,1,0,2,2,2,2,0,2,2,0,2,0,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,2,2,0,2,2,2,2,2,2,0,2,2,2,2,0,1,1,0,0,0,0,2,2,2,2,0,0,2,0,0,2,2,2,2,0,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,0,1,1,0,0,2,0,0,0,2,2,0,2,0,2,2,2,2,2,0,2,0,0,2,2,0,2,2,0,2,2,2,0,0,2,2,2,2,0,2,2,2,0,0,1,1,0,2,2,2,0,2,0,2,2,0,2,2,2,0,2,2,2,0,2,0,2,2,0,2,2,2,2,2,2,2,0,2,0,2,2,2,2,0,2,2,0,1,1,0,2,0,2,0,2,2,0,0,2,2,2,2,0,2,2,2,2,2,2,2,0,2,0,0,0,0,0,2,0,0,2,2,0,2,2,2,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,89,82,95,24,35,69,73,71,23,5,87,90,41,96,87,87,72,81,29,20,53,96,2,8,39,33,34,13,46,62,86,8,11,11,32,39,61,76,43,42,88,15,27,80,16,28,78,86,36,49,77,74,3,72,28,18,54,58,72,17,78,93,13,29,86,61,31,89,6,1,66,51,68,42,39,27,65,2,83,12,75,75,92,19,75,50,62,10,2,72,56,65,15,57,28,79,47,68,41,86,90,75,96,53,61,57,83,23,76,44,9,40,6,64,94,36,68,57,12,18,56,16,66,39,35,93,68,90,7,41,42,93,93,48,45,69,34,88,9,18,90,15,89,20,37,84,96,63,34,81,88,35,8,7,66,92,60,1,9,32,86,1,50,59,85,49,2,89,53,24,44,61,43,3,86,23,39,32,3,33,51,98,66,58,57,56,27,29,74,64,1,16,68,3,51,70,95,14,19,54,17,61,29,28,18,4,8,30,21,50,10,18,8,40,91,16,64,68,11,59,84,98,10,92,18,59,85,84,24,48,72,50,16,9,19,10,79,77,23,15,7,3,37,40,88,35,61,66,98,5,74,47,92,50,79,73,11,43,25,93,42,53,46,73,52,64,48,47,64,73,17,69,16,22,14,46,29,3,69,15,13,86,3,82,17,69,78,86,69,23,48,74,22,13,75,15,39,21,12,17,13,12,70,36,88,16,21,22,88,2,3,55,58,7,85,53,73,79,66,61,39,12,42,71,72,95,22,48,34,68,55,6,40,93,97,26,4,56,95,39,70,51,45,75,94,49,58,90,82,12,94,22,34,57,83,79,8,96,84,28,91,8,10,2,17,21,42,67,73,64,38,40,81,57,15,93,70,26,74,31,96,75,16,39,67,46,37,68,98,5,15,3,84,97,71,73,1,27,65,40,23,74,22,29,49,66,62,96,71,85,40,78,9,30,40,29,68,38,88,50,95,12,49,94,84,21,73,72,52,39,51,19,87,42,8,24,42,71,3,82,65,97,38,42,98,81,31,81,47,33,91,25,34,96,28,46,18,63,29,26,21,22,97,58,29,16,1,38,31,76,39,22,69,98,41,36,29,24,63,66,43,55,72,72,79,80,62,80,70,73,49,29,11,3,84,76,20,35,40,11,47,17,33,31,32,70,38,53,54,11,4,29,38,18,89,27,96,27,57,3,64,83,3,48,28,67,38,6,72,96,8,51,86,1,1,88,70,87,40,34,71,68,74,77,52,38,64,55,17,63,9,41,29,46,93,23,93,11,78,25,21,79,76,3,62,25,18,72,1,9,22,66,81,9,30,60,91,23,72,29,96,36,56,14,67,73,82,1,62,15,86,49,56,97,97,95,39,2,10,58,51,62,3,4,34,35,79,47,14,94,49,66,76,74,35,47,63,31,93,31,71,23,39,87,91,7,36,3,65,12,90,78,14,63,25,74,82,67,98,46,28,66,42,60,50,58,42,90,44,93,4,72,84,26,10,76,17,93,22,83,73,39,81,1,40,36,21,35,66,40,51,5,7,37,64,86,68,46,54,64,30,25,33,69,54,94,48,55,10,6,16,28,47,86,31,44,10,12,98,1,51,31,88,35,31,87,6,44,95,36,2,95,91,7,45,5,28,30,35,88,66,18,42,44,21,60,65,35,64,53,96,73,36,11,22,80,34,28,90,7,77,21,96,84,75,19,9,31,96,67,33,94,26,34,45,3,59,26,47,57,57,20,49,97,39,83,29,92,11,6,58,25,22,89,78,69,77,48,3,44,64,67,19,80,89,41,6,47,41,67,91,38,83,83,38,12,29,39,5,5,23,9,23,63,69,69,67,60,34,27,32,49,22,23,93,44,47,24,63,87,95,80,36,85,2,95,82,35,49,44,96,3,83,83,61,76,92,42,52,43,29,52,72,70,50,97,93,84,57,85,25,95,56,57,49,70,48,77,94,78,23,22,96,86,65,43,90,42,47,56,48,56,39,63,48,14,5,67,20,56,5,50,74,6,22,58,91,34,12,26,12,66,88,31,71,64,82,86,32,40,56,19,40,86,51,56,4,13,48,11,32,76,80,2,61,58,7,70,44,83,49,89,80,2,30,4,34,49,75,23,94,47,61,68,88,28,17,76,58,74,87,21,28,21,48,97,17,41,82,7,5,48,89,14,41,76,23,72,52,1,3,15,72,10,79,87,78,7,33,79,12,21,54,36,91,73,15,89,26,27,39,7,28,7,88,95,41,69,97,80,72,78,35,15,43,33,21,91,59,97,6,56,34,44,16,15,21,4,25,13,22,56,75,75,98,85,4,70,49,61,83,2,24,20,20,82,21,62,12,90,78,71,15,80,56,98,73,83,26,82,95,60,30,62,50,84,10,25,89,73,54,36,10,32,43,29,5,22,20,54,48,17,42,84,47,14,58,48,70,23,44,70,63,28,86,46,57,57,86,78,12,21,46,60,48,10,19,98,91,87,63,25,9,89,41,39,4,83,33,83,28,41,68,66,78,24,68,52,36,59,4,12,5,2,13,35,35,65,924596]


tiles = {}


def run_code(code):
    input_queue, output_queue = queue.Queue(), queue.Queue()
    machine = IntcodeMachine(input_queue, output_queue, code)
    processor = threading.Thread(target=machine.compute, daemon=True)

    max_x = 0
    max_y = 0

    processor.start()
    while processor.is_alive():
        x = output_queue.get()
        if x > max_x:
            max_x = x
        y = output_queue.get()
        if y > max_y:
            max_y = y
        tile = output_queue.get()

        tiles['{},{}'.format(x, y)] = tile
    processor.join()

    game_map = [[' ' for x in range(max_x + 1)] for y in range(max_y + 1)]

    blocks = 0
    for tile in tiles:
        coords = tile.split(',')
        if tiles[tile] == 0:
            drawing = ' '
        elif tiles[tile] == 1:
            drawing = 'X'
        elif tiles[tile] == 2:
            drawing = '#'
            blocks += 1
        elif tiles[tile] == 3:
            drawing = '='
        elif tiles[tile] == 4:
            drawing = 'O'
        game_map[int(coords[1])][int(coords[0])] = drawing

    for row in game_map:
        print(''.join(row))
        
    print('\n{}'.format(blocks))


if __name__ == '__main__':
    run_code(input_code)

import pygame
 
pygame.init()
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 90
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    minutes = total_seconds // 60
 
    seconds = total_seconds % 60
 
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    print output_string
    frame_count += 1
    clock.tick(frame_rate)
 
    # Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
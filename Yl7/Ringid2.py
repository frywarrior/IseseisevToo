import pygame, numpy # impordib pygame ja numpy

screen, im = pygame.display.set_mode([640, 480]), 8  # loob ekraani suurusega 640 x 480 ja ringi suuruse

class Ring: # loob klassi nimega Ring
    def __init__(self): # lisab enda muutujad
        self.xy = pygame.mouse.get_pos() # võtab hiirepostisiooni
        self.color = list(numpy.random.choice(range(256), size=3)) # seab suvalise väri
        self.size = im # seab ringi suuruse enda jaoks

    def draw(self): # joonistamise funktsioon
        pygame.draw.circle(screen, self.color, self.xy, self.size, 1) # joonistab ringi oma parameetritega

ringid = [] # loob uue listi nimega ringid

while True:  # kui on tõene
    screen.fill([0, 0, 0]) # täidab ekraani mustaga
    for i in pygame.event.get():  # võtab evendid
        if i.type == pygame.QUIT:  # kui kasutaja vajutab "X" nupule
            quit()  # väljub mängust
        if i.type == pygame.MOUSEBUTTONDOWN:  # kui hiirenupp on all
            ringid.append(Ring()) # lisab ringid listi
            if im >= 48:  # kui ringi suurus on suurem või võrdne 48, siis
                del ringid[0] # kustutab esimese ringi listist
            im += 4  # Uuendab järgmise ringi suurust
    for ring in ringid: # iga ringi kohta ringi listis
        ring.draw() # joonistab ringi
    pygame.display.flip()  # uuendab ekraani

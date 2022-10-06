import sys
from threading import Thread
from pygame import *
from Models.Planetas import *
from Models.Nave import *
from Models.Nodriza import *
from Models.Arbol import *
from Naves import *
from Sistema import *


class ACME():
    def __init__(self):
        self.aux = 1  # AUX = Tiempo global
        self.destruir_planeta = None
        self.btn_vel = boton_x1
        self.btn_temp = boton_30s
        self.temporizador = 30

    def reloj(self, time, screen):
        reloj_text = fuente.render(
            f"TIME: {self.aux}", 1, fuente_color, fuente_bg)
        if self.aux == time:
            time_aux = self.aux
            self.aumentar_materiales(time_aux)
            if time_aux % self.temporizador == 0:
                self.despachar_naves()
            self.aux += 1
        screen.blit(reloj_text, (1100, 20))

    def contadores(self, screen):
        nodriza_almacen = fuente.render(
            f"ALMACEN: {naves.nodriza.materiales.sumar(naves.nodriza.materiales)}", 1, fuente_color, fuente_bg)
        nodriza_materiales = fuente.render(
            f"MATERIALES (#N): {naves.nodriza.materiales.total_nodos(naves.nodriza.materiales)}", 1, fuente_color, fuente_bg)

        nave1_almacen = fuente.render(
            f"{naves.nave1.nombre}: {naves.nave1.cantidad}", 1, fuente_color, fuente_bg)
        nave1_nodos = fuente.render(
            f"#N: {naves.nave1.get_nodos()}", 1, fuente_color, fuente_bg)

        nave2_almacen = fuente.render(
            f"{naves.nave1.nombre}: {naves.nave2.cantidad}", 1, fuente_color, fuente_bg)
        nave2_nodos = fuente.render(
            f"#N: {naves.nave2.get_nodos()}", 1, fuente_color, fuente_bg)

        nave3_almacen = fuente.render(
            f"{naves.nave1.nombre}: {naves.nave3.cantidad}", 1, fuente_color, fuente_bg)
        nave3_nodos = fuente.render(
            f"#N: {naves.nave3.get_nodos()}", 1, fuente_color, fuente_bg)

        screen.blit(nodriza_almacen, (0, 150))
        screen.blit(nodriza_materiales, (0, 170))

        screen.blit(nave1_almacen, (0, 0))
        screen.blit(
            nave1_nodos, (0+(nave1_almacen.get_width()-nave1_nodos.get_width())/2, 20))

        screen.blit(nave2_almacen, (200, 0))
        screen.blit(
            nave2_nodos, (200+(nave2_almacen.get_width()-nave2_nodos.get_width())/2, 20))

        screen.blit(nave3_almacen, (400, 0))
        screen.blit(
            nave3_nodos, (400+(nave3_almacen.get_width()-nave3_nodos.get_width())/2, 20))

    def aumentar_materiales(self, time):
        if time % 10 == 0:
            planetas = sistema.arbol.inorder(sistema.arbol)
            for planet in planetas:
                planet.cantidad += 2
            self.planetas_data()

    def despachar_naves(self):
        nave = naves.obtener_disponible()
        ruta = randint(1, 6)
        if nave == naves.nave1 and stop_threads == False:
            self.thread_nave1 = Thread(target=lambda: self.mover_nave(
                naves.nave1, self.rutas(ruta)))
            threads.append(self.thread_nave1)
            self.thread_nave1.start()

        if nave == naves.nave2 and stop_threads == False:
            self.thread_nave2 = Thread(target=lambda: self.mover_nave(
                naves.nave2, self.rutas(ruta)))
            threads.append(self.thread_nave2)
            self.thread_nave2.start()

        if nave == naves.nave3 and stop_threads == False:
            self.thread_nave3 = Thread(target=lambda: self.mover_nave(
                naves.nave3, self.rutas(ruta)))
            threads.append(self.thread_nave3)
            self.thread_nave3.start()

    def rutas(self, ran):
        if ran == 1:
            #print("Recorrido: "+"1")
            return sistema.arbol.inorder(sistema.arbol)
        if ran == 2:
            #print("Recorrido: "+"2")
            return sistema.arbol.preorder(sistema.arbol)
        if ran == 3:
            #print("Recorrido: "+"3")
            return sistema.arbol.postorder(sistema.arbol)
        if ran == 4:
            #print("Recorrido: "+"4")
            return sistema.arbol.inorderR(sistema.arbol)
        if ran == 5:
            #print("Recorrido: "+"5")
            return sistema.arbol.preorderR(sistema.arbol)
        if ran == 6:
            #print("Recorrido: "+"6")
            return sistema.arbol.postorderR(sistema.arbol)

    def mover_nave(self, nave, ruta):
        if nave.disponible:
            nave.disponible = False
            # print(ruta)
            #print(f"{nave.nombre}: Iniciando recorrido")
            for planeta in ruta:
                if stop_threads:
                    return
                #print(f"{nave.nombre}: moviendose a: "+planeta.nombre)
                while not (stop_threads and planeta is None):
                    if planeta is None or planeta.explotado == True:
                        break
                    if stop_threads:
                        return
                    if (naves.mover(nave, planeta)):
                        planeta.visitas += 1
                        self.recolectar_materiales(nave, planeta)
                        sleep(1)
                        break
                    sleep(0.01)
                if nave.cantidad == 30:
                    break
            while not stop_threads:
                if stop_threads:
                    return
                if (naves.mover(nave, naves.nodriza)):
                    self.guardar_materiales(nave)
                    break
                sleep(0.02)
            #print(f"{nave.nombre}: Terminando Recorrido")
            nave.disponible = True

    def planetas_data(self):
        if stop_threads == True:
            return
        filename = "./Data/planetas.json"
        entry = [
            sistema.pluton.toString(),
            sistema.triton.toString(),
            sistema.beltrak.toString(),
            sistema.zork.toString(),
            sistema.yari.toString(),
            sistema.mercurio.toString(),
            sistema.tarca.toString(),
            sistema.zulman.toString(),
        ]

        with open(filename, mode='r+') as file:
            file.seek(0)
            json.dump(entry, file)
            file.truncate()

    def recolectar_materiales(self, nave, planeta):
        if nave.cantidad < 30:
            cantidad = 30 - nave.cantidad
            recurso = planeta.get_material(cantidad)
            recurso["fecha"] = self.aux
            nave.almacen.append(recurso)
            nave.set_cantidad()
            #print(f"Almacen: {nave.almacen}")

    def guardar_materiales(self, nave):
        if nave.cantidad == 30:
            recurso = nave.get_material()
            naves.nodriza.almacen.append(recurso)
            for i in naves.nodriza.almacen:
                naves.nodriza.agregar_materiales(i)
            naves.nodriza.almacen = []
            naves.nodriza.cantidad = 0
        # print(naves.nodriza.materiales.mostrar())

    def dibujar_boton(self, boton, color, mensaje):
        boton = draw.rect(screen, color, boton, 0)
        text = fuente.render(mensaje, 1, fuente_color)
        screen.blit(text, (boton.x+(boton.width-text.get_width())/2,
                           boton.y+(boton.height-text.get_height())/2))

    def boton_planeta(self, planeta):
        color = (88, 88, 88)
        if planeta.explotado == True:
            color = (255, 0, 0)
        elif planeta == self.destruir_planeta and planeta.visitas > 0:
            color = (0, 255, 0)
        elif planeta.visitas > 0:
            color = (255, 255, 255)
        return color

    def panel_planetas(self, panel):
        fuente_color = (0, 0, 0)
        draw.rect(screen, (0, 0, 0), panel, 0)
        self.pluton_panel = draw.rect(
            screen, self.boton_planeta(sistema.pluton), (15, 490, 45, 45))
        self.triton_panel = draw.rect(
            screen, self.boton_planeta(sistema.triton), (62, 490, 45, 45))
        self.beltrak_panel = draw.rect(
            screen, self.boton_planeta(sistema.beltrak), (109, 490, 45, 45))
        self.zork_panel = draw.rect(
            screen, self.boton_planeta(sistema.zork), (15, 545, 45, 45))
        self.yari_panel = draw.rect(
            screen, self.boton_planeta(sistema.yari), (62, 545, 45, 45))
        self.mercurio_panel = draw.rect(
            screen, self.boton_planeta(sistema.mercurio), (109, 545, 45, 45))
        self.tarca_panel = draw.rect(
            screen, self.boton_planeta(sistema.tarca), (32, 598, 45, 45))
        self.zulman_panel = draw.rect(
            screen, self.boton_planeta(sistema.zulman), (85, 598, 45, 45))

        pluton_text = fuente.render("100", 1, fuente_color)
        triton_text = fuente.render("150", 1, fuente_color)
        beltrak_text = fuente.render("200", 1, fuente_color)
        zork_text = fuente.render("120", 1, fuente_color)
        yari_text = fuente.render("110", 1, fuente_color)
        mercurio_text = fuente.render("50", 1, fuente_color)
        tarca_text = fuente.render("20", 1, fuente_color)
        zulman_text = fuente.render("80", 1, fuente_color)

        screen.blit(pluton_text, (self.pluton_panel.x+(self.pluton_panel.width-pluton_text.get_width()
                                                       )/2, self.pluton_panel.y+(self.pluton_panel.height-pluton_text.get_height())/2))
        screen.blit(triton_text, (self.triton_panel.x+(self.triton_panel.width-triton_text.get_width()
                                                       )/2, self.triton_panel.y+(self.triton_panel.height-triton_text.get_height())/2))
        screen.blit(beltrak_text, (self.beltrak_panel.x+(self.beltrak_panel.width-beltrak_text.get_width()
                                                         )/2, self.beltrak_panel.y+(self.beltrak_panel.height-beltrak_text.get_height())/2))
        screen.blit(zork_text, (self.zork_panel.x+(self.zork_panel.width-zork_text.get_width()
                                                   )/2, self.zork_panel.y+(self.zork_panel.height-zork_text.get_height())/2))
        screen.blit(yari_text, (self.yari_panel.x+(self.yari_panel.width-yari_text.get_width()
                                                   )/2, self.yari_panel.y+(self.yari_panel.height-yari_text.get_height())/2))
        screen.blit(mercurio_text, (self.mercurio_panel.x+(self.mercurio_panel.width-mercurio_text.get_width()
                                                           )/2, self.mercurio_panel.y+(self.mercurio_panel.height-mercurio_text.get_height())/2))
        screen.blit(tarca_text, (self.tarca_panel.x+(self.tarca_panel.width-tarca_text.get_width()
                                                     )/2, self.tarca_panel.y+(self.tarca_panel.height-tarca_text.get_height())/2))
        screen.blit(zulman_text, (self.zulman_panel.x+(self.zulman_panel.width-zulman_text.get_width()
                                                       )/2, self.zulman_panel.y+(self.zulman_panel.height-zulman_text.get_height())/2))

    def color_btn(self, boton, actual):
        color = (0, 0, 0)
        if boton == actual:
            color = (0, 255, 0)
        return color

    def cambio_vel(self):
        if boton_x05.collidepoint(mouse.get_pos()) and self.btn_vel != boton_x05:
            self.btn_vel = boton_x05
            naves.velocidad = (velocidad*0.5)
        if boton_x1.collidepoint(mouse.get_pos()) and self.btn_vel != boton_x1:
            self.btn_vel = boton_x1
            naves.velocidad = (velocidad*1)
        if boton_x2.collidepoint(mouse.get_pos()) and self.btn_vel != boton_x2:
            self.btn_vel = boton_x2
            naves.velocidad = (velocidad*2)
        if boton_x5.collidepoint(mouse.get_pos()) and self.btn_vel != boton_x5:
            self.btn_vel = boton_x5
            naves.velocidad = (velocidad*5)

    def cambio_temp(self):
        if boton_5s.collidepoint(mouse.get_pos()) and self.btn_temp != boton_5s:
            self.btn_temp = boton_5s
            self.temporizador = 5
        if boton_10s.collidepoint(mouse.get_pos()) and self.btn_temp != boton_10s:
            self.btn_temp = boton_10s
            self.temporizador = 10
        if boton_30s.collidepoint(mouse.get_pos()) and self.btn_temp != boton_30s:
            self.btn_temp = boton_30s
            self.temporizador = 30
        if boton_60s.collidepoint(mouse.get_pos()) and self.btn_temp != boton_60s:
            self.btn_temp = boton_60s
            self.temporizador = 60

    def destruir(self, planeta):
        try:
            print(f"ELIMINANDO {planeta.nombre}... 3... 2... 1...")
            planeta.explotado = True
            sistema.arbol.delete(sistema.arbol, planeta)
        except:
            print("PLANETA YA EXPLOTADO")

    def explosion(self, screen):
        exp_img = pygame.image.load("./Resources/explosion.png")
        exp_img = pygame.transform.scale(exp_img, (200, 200))
        if sistema.pluton.explotado:
            screen.blit(exp_img, sistema.pluton.rect)
        if sistema.triton.explotado:
            screen.blit(exp_img, sistema.triton.rect)
        if sistema.beltrak.explotado:
            screen.blit(exp_img, sistema.beltrak.rect)
        if sistema.zork.explotado:
            screen.blit(exp_img, sistema.zork.rect)
        if sistema.yari.explotado:
            screen.blit(exp_img, sistema.yari.rect)
        if sistema.mercurio.explotado:
            screen.blit(exp_img, sistema.mercurio.rect)
        if sistema.tarca.explotado:
            screen.blit(exp_img, sistema.tarca.rect)
        if sistema.zulman.explotado:
            screen.blit(exp_img, sistema.zulman.rect)

    def detener_hilos(self):
        for thread in threads:
            thread.join()

    def pulsar_botones(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == True:
            if self.pluton_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.pluton
            if self.triton_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.triton
            if self.beltrak_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.beltrak
            if self.zork_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.zork
            if self.yari_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.yari
            if self.mercurio_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.mercurio
            if self.tarca_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.tarca
            if self.zulman_panel.collidepoint(mouse.get_pos()):
                self.destruir_planeta = sistema.zulman

            self.cambio_vel()
            self.cambio_temp()

            if destruir_planeta.collidepoint(mouse.get_pos()):
                try:
                    print(f"Planeta escogido {self.destruir_planeta.nombre}")
                    if self.destruir_planeta.visitas > 0:
                        self.destruir(self.destruir_planeta)
                    else:
                        print("Planeta sin visitas")
                except:
                    print("Sin planeta escogido")


def main():
    global sistema, naves, stop_threads, threads, temporizador, velocidad
    global boton_x05, boton_x1, boton_x2, boton_x5, destruir_planeta, boton_5s, boton_10s, boton_30s, boton_60s
    global btn_vel, btn_temp

    ends = False
    velocidad = 2

    destruir_planeta = Rect(10, 660, 150, 50)
    panel_planetas = Rect(10, 480, 149, 170)

    boton_x05 = Rect(170, 660, 50, 50)
    boton_x1 = Rect(170, 600, 50, 50)
    boton_x2 = Rect(170, 540, 50, 50)
    boton_x5 = Rect(170, 480, 50, 50)

    boton_5s = Rect(230, 660, 50, 50)
    boton_10s = Rect(230, 600, 50, 50)
    boton_30s = Rect(230, 540, 50, 50)
    boton_60s = Rect(230, 480, 50, 50)

    sistema = Sistema()
    naves = Naves(velocidad)
    acme = ACME()
    threads = []

    clock = pygame.time.Clock()

    while not ends:

        time = int(pygame.time.get_ticks()/1000)

        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_threads = True
                acme.detener_hilos()
                ends = True
                sys.exit()
            acme.pulsar_botones(event)

        # ----------------------------------------- PROGRAMA ---------------------------------------

        sistema.mostrar(screen)
        sistema.contadores(screen)

        acme.reloj(time, screen)
        acme.contadores(screen)
        acme.panel_planetas(panel_planetas)
        acme.explosion(screen)

        acme.dibujar_boton(destruir_planeta, (0, 0, 0), "DESTRUIR")
        acme.dibujar_boton(boton_x05, acme.color_btn(
            boton_x05, acme.btn_vel), "x0.5")
        acme.dibujar_boton(boton_x1,  acme.color_btn(
            boton_x1, acme.btn_vel), "x1")
        acme.dibujar_boton(boton_x2,  acme.color_btn(
            boton_x2, acme.btn_vel), "x2")
        acme.dibujar_boton(boton_x5,  acme.color_btn(
            boton_x5, acme.btn_vel), "x5")

        acme.dibujar_boton(boton_5s, acme.color_btn(
            boton_5s, acme.btn_temp), "5s")
        acme.dibujar_boton(boton_10s,  acme.color_btn(
            boton_10s, acme.btn_temp), "10s")
        acme.dibujar_boton(boton_30s,  acme.color_btn(
            boton_30s, acme.btn_temp), "30s")
        acme.dibujar_boton(boton_60s,  acme.color_btn(
            boton_60s, acme.btn_temp), "60s")

        naves.mostrar(screen)

        # --------------------------------------- FIN PROGRAMA -------------------------------------

        pygame.display.flip()
        clock.tick(120)


global fuente, fuente_color, fuente_bg

pygame.init()

threads = []
stop_threads = False
size = width, height = 1280, 720
main_background = pygame.image.load("./Resources/space.jpg")
screen = pygame.display.set_mode(size)
fuente = pygame.font.SysFont("Roboto", 30)
fuente_color = (255, 255, 255)
fuente_bg = (0, 0, 0)

pygame.display.set_caption("SISTEMA ACME")

main()

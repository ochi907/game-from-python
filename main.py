import pygame
import imgui
import sys
from imgui.integrations.pygame import PygameRenderer
import OpenGL.GL as gl
import os

def main():
    pygame.init()
    # กำหนดขนาดเริ่มต้น (หน้าต่างปกติ)
    initial_size = (1280, 720)

    # เพิ่ม pygame.RESIZABLE เพื่อให้กดขยายหน้าต่างได้
    screen = pygame.display.set_mode(initial_size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
    pygame.display.set_caption("Gemini AI - Responsive System")

    imgui.create_context()
    renderer = PygameRenderer()

    io = imgui.get_io()
    
    # โหลดฟอนต์ภาษาไทย
    script_dir = os.path.dirname(__file__)
    font_path = os.path.join(script_dir, "font", "Chandler42 Regular.otf")
    if os.path.exists(font_path):
        io.fonts.add_font_from_file_ttf(font_path, 22, io.fonts.get_glyph_ranges_thai())
        renderer.rebuild_font_atlas()

    # สถานะหน้าต่าง
    show_weather = False
    show_editor = False
    text_content = "พิมพ์ข้อความที่นี่..."
    weather_info = {"city": "Rayong", "temp": "30°C", "status": "Cloudy", "humidity": "75%"}

    running = True
    while running:
        # --- หัวใจสำคัญของการแก้บั๊ก: ดึงขนาดหน้าจอที่ "แท้จริง" ณ วินาทีนั้น ---
        current_w, current_h = pygame.display.get_surface().get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            renderer.process_event(event)
        
        renderer.process_inputs()

        # อัปเดตพิกัดให้ ImGui รู้ว่าตอนนี้โลกกว้างขึ้นแค่ไหน (แก้บั๊กเมาส์ไม่ตรง/จอเบี้ยว)
        io.display_size = (current_w, current_h)
        # ปรับพิกัด Viewport ของ OpenGL ให้เต็มขนาดหน้าต่างใหม่ด้วย
        gl.glViewport(0, 0, current_w, current_h)

        imgui.new_frame()

        # --- Menu Bar ---
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu('File', True):
                if imgui.menu_item('Quit', 'Alt+F4')[0]:
                    running = False
                imgui.end_menu()

            if imgui.begin_menu('Tool', True):
                if imgui.menu_item('Weather Dashboard', None, show_weather)[0]:
                    show_weather = not show_weather
                if imgui.menu_item('Type Editor', None, show_editor)[0]:
                    show_editor = not show_editor
                imgui.end_menu()
            imgui.end_main_menu_bar()

        # --- Weather Dashboard (ปรับตามขนาดจอ) ---
        if show_weather:
            # ใช้การคำนวณตำแหน่งและขนาดแบบสัมพันธ์กับจอ (เช่น กว้าง 1 ใน 4 ของจอ)
            imgui.set_next_window_size(350, 250, condition=imgui.FIRST_USE_EVER)
            expanded, show_weather = imgui.begin("Weather Dashboard", True)
            if expanded:
                imgui.text(f"Location: {weather_info['city']}")
                imgui.separator()
                imgui.text_colored(f"Temp: {weather_info['temp']}", 1.0, 0.5, 0.0)
                imgui.text(f"Status: {weather_info['status']}")
            imgui.end()

        # --- Type Editor (ปรับตามขนาดจอ) ---
        if show_editor:
            # ให้ Editor ขยายใหญ่เกือบเต็มจอเสมอ ไม่ว่าจะย่อหรือขยายหน้าต่างหลัก
            imgui.set_next_window_size(current_w * 0.8, current_h * 0.7, condition=imgui.FIRST_USE_EVER)
            expanded, show_editor = imgui.begin("Type Editor", True)
            if expanded:
                changed, text_content = imgui.input_text_multiline(
                    "##editor", text_content, buffer_length=10000, 
                    width=-1, height=-1 # -1 หมายถึงขยายให้เต็มพื้นที่หน้าต่างย่อย
                )
            imgui.end()

        # --- Rendering ---
        gl.glClearColor(0.05, 0.05, 0.05, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        renderer.render(imgui.get_draw_data())
        pygame.display.flip()

    renderer.shutdown()
    pygame.quit()

if __name__ == "__main__":
    main()
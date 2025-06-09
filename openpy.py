import OpenGL.GL as gl
import glfw

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Hello OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()


# This function will be executed each frame
    def render():
    # Draw a rectangle
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3f(1, 0, 0)  # Red color
        gl.glVertex2f(-0.5, -0.5)
        gl.glVertex2f(0.5, -0.5)
        gl.glVertex2f(0.5, 0.5)
        gl.glVertex2f(-0.5, 0.5)
        gl.glEnd()

# In the main loop of your application, call the render function:
# ...
    while not glfw.window_should_close(window):
    # ... (other code)

    # Render here
        render()

    # ...



    glfw.terminate()

if __name__ == "__main__":
    main()


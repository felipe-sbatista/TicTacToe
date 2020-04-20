
VERTEX_SHADER = """
    #version 410
    in vec4 position;

    void main()
    {
        gl_Position = position;
    }

    """

FRAGMENT_SHADER = """
    #version 410
    out vec4 frag_color; 
     void main()
     {
        frag_color = vec4(1.0f,0.0f,0.0f,1.0f);
     }
    """

VIEW_WIDTH = 640
VIEW_HEIGHT = 480
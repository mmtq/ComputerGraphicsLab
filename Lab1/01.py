# Regenerate the animation with persistent streams (no "dark" frames)
stream_positions = [random.randint(-20, 0) for _ in range(columns)]
stream_speeds = [random.randint(1, 2) for _ in range(columns)]
frames = []

# Create bright stream trail and persistent background
for _ in range(40):  # ~5 seconds at 8 fps
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)

    for col in range(columns):
        drop_pos = stream_positions[col]
        for row in range(rows):
            if row <= drop_pos:
                char = random.choice(python_chars)
                x = col * font_size
                y = row * font_size

                # Make the head of the stream brighter
                if row == drop_pos:
                    fill = (180, 255, 180)  # bright green
                else:
                    green_value = max(0, 255 - (drop_pos - row) * 15)
                    fill = (0, green_value, 0)

                draw.text((x, y), char, font=font, fill=fill)

        stream_positions[col] += stream_speeds[col]
        if stream_positions[col] > rows + random.randint(5, 15):
            stream_positions[col] = random.randint(-20, 0)

    frames.append(img)

# Save improved animation
gif_path = "/mnt/data/matrix_python_code_no_dark.gif"
frames[0].save(
    gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=125,
    loop=0
)

gif_path

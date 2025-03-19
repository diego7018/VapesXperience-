import urllib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Diccionario de imágenes alojadas en Imgur
imgur_images = {
    "logo": "https://i.postimg.cc/9z54z8cm/APROVADO-POR-LA-RANA.png",
    "whatsapp": "https://i.postimg.cc/DfCZm564/whatsapp-icon-vector-20891422.jpg",
    "facebook": "https://i.postimg.cc/9z54z8cm/APROVADO-POR-LA-RANA.png",
    "instagram": "https://i.postimg.cc/T3vmPwPV/c-HJpdm-F0-ZS9p-ZXQv-d2-Vic2l0-ZS8y-MDIy-LTA1-L3-Jt-NTMz-LW5lb24t-MDAz-Lmpw-Zw-pjg.webp",
    "banners": [
        "https://i.postimg.cc/Dy7hnqng/53910cd7-6829-4fe8-996a-2048da3b1b73.png",
        "https://i.postimg.cc/d1TsZvxj/dcea8551-1b1b-4eff-8afc-43ac08d5b233.png",
        "https://i.postimg.cc/CLtQc94P/c7452781-0880-41cb-88dc-652a830fe9fe.jpg",
    ],
    "products": [
        "https://i.postimg.cc/ydJpHPn6/Whats-App-Image-2025-03-18-at-3-51-27-PM-1.jpg",
        "https://i.postimg.cc/sgRk4tmY/abf90983-24b2-4360-a416-e94e78573b83.jpg",
        "https://i.postimg.cc/V6B1jzQb/Whats-App-Image-2025-03-18-at-3-51-28-PM.jpg",
        "https://i.postimg.cc/TwXfLpS6/Whats-App-Image-2025-03-18-at-3-51-27-PM.jpg",
        "https://i.postimg.cc/3JgvqvXs/Whats-App-Image-2025-03-18-at-3-53-53-PM.jpg",
        "https://i.postimg.cc/PrqhwG6P/Whats-App-Image-2025-03-18-at-3-54-47-PM.jpg",
        "https://i.postimg.cc/bYgprY97/Whats-App-Image-2025-03-18-at-3-52-37-PM.jpg",
        "https://i.postimg.cc/c45W7DjT/Whats-App-Image-2025-03-18-at-3-56-54-PM.jpg",
        "https://i.postimg.cc/Vvfwg2mZ/Whats-App-Image-2025-03-18-at-3-56-53-PM.jpg",
    
    ],
    "product_titles": [
        "LIFE POD LOVE 66", "LIFE POD GRAPE HONEYDEW ", "LIFE POD PINK LEMONADE", "LIFE POD BLACKBERRY ICE", "DRAGBAR 3000 PUFFS",
        "DRAGBAR 3000 PUFFS", "DRAGBAR 3000 PUFFS", "VOOPOO MAX 16K", "VOOPOO MAX 16K", "ASPIRE NAUTILUS",
        "INNOKIN ENDURA", "JOYETECH EGO"
    ],
    "product_prices": [
        "S/120", "S/120", "S/120", "S/120", "S/49.90",
        "S/49.90", "S/49.90", "S/140", "S/140", "S/140",
        "S/55.00", "S/55.00"
    ]
}
@app.get("/", response_class=HTMLResponse)
async def home():
    banners_html = "".join(
        f'<div class="carousel-item"><img src="{img}" alt="Banner {i+1}"></div>'
        for i, img in enumerate(imgur_images["banners"])
    )

    product_html = "".join(
    f'<div class="product">'
    f'<img src="{img}" alt="Producto {i+1}">'
    f'<p class="product-title"><strong>{imgur_images["product_titles"][i]}</strong><br>{imgur_images["product_prices"][i]}</p>'
    f'<a href="https://wa.me/900070749?text='
    f'Hola, quiero adquirir este producto.%0A'  # Mensaje inicial
    f'*{imgur_images["product_titles"][i]}*%0A'  # Nombre del producto en negrita
    f'*Precio:* {imgur_images["product_prices"][i]}%0A'  # Precio en negrita
    f'{img}" target="_blank">'  # Imagen como enlace
    f'<button class="buy-button">COMPRAR</button>'
    f'</a>'
    f'</div>'
    for i, img in enumerate(imgur_images["products"])
)

    

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VAPESXPERIENCE</title>
        <link rel="icon" type="image/png" href="{imgur_images['logo']}">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Arial', sans-serif;
            }}
            body {{
                background-color: #ffffff;
                color: #333;
                text-align: center;
                overflow-x: hidden;
            }}
            /* Barra de navegación */
            .menu {{
                background-color: black;
                padding: 15px 20px;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
                z-index: 1000;
            }}
            .menu-logo {{
                color: white;
                font-size: 35px;
                font-weight: bold;
                text-align: center; /* Centra el texto */
                flex: 2; /* Hace que ocupe todo el espacio disponible */
                margin-left: 240px; /* Ajusta este valor según necesites */
            }}
            .menu-items {{
                display: flex;
                list-style: none;
            }}
            .menu-items li {{
                margin: 0 15px;
            }}
            .menu-items a {{
                text-decoration: none;
                color: white;
                font-size: 16px;
                font-weight: bold;
                transition: color 0.4s;
            }}
            .menu-items a:hover {{
                color: #ff9900;
            }}
            /* Carrusel */
            .carousel-container {{
                width: 100%;
                height: 99vh;
                overflow: hidden;
                margin-top: 50px;
            }}
            .carousel {{
                display: flex;
                width: {100 * len(imgur_images["banners"])}%;
                transition: transform 1.5s ease-in-out;
            }}
            .carousel-item {{
                flex: 1;
                width: {100 / len(imgur_images["banners"])}%;
            }}
            .carousel img {{
                width: 100%;
                height: 100%;
                object-fit: contain;
            }}
            /* Productos */
            .products {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                padding: 20px;
            }}
            .product {{
                width: 300px;
                margin: 10px;
                text-align: center;
            }}
            .product img {{
                width: 100%;
                height: auto;
                border-radius: 5px;
            }}
            .product-title {{
                font-size: 14px;
                margin: 5px 0;
            }}
            .buy-button {{
                background-color: black;
                color: white;
                border: none;
                padding: 8px 15px;
                cursor: pointer;
                font-size: 14px;
                border-radius: 5px;
            }}
            .buy-button:hover {{
                background-color: #ff9900;
            }}
            /* Botones de redes sociales */
            .social-buttons {{
                position: fixed;
                bottom: 180px;
                right: 20px;
                display: flex;
                flex-direction: column;
                gap: 10px;
                z-index: 1000;
            }}
            .social-buttons img {{
                width: 50px;
                height: 50px;
                cursor: pointer;
                border-radius: 50%;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            }}
            /* Botón de WhatsApp */
            .whatsapp-button {{
                position: fixed;
                bottom: 55px;
                right: 20px;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                cursor: pointer;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                z-index: 1000;
            }}
            /* Animación de banners */
            @keyframes deslizar {{
                from {{ transform: translateX(100%); }}
                to {{ transform: translateX(-100%); }}
            }}
        </style>
    </head>
    <body>
        <nav class="menu">
            <div class="menu-logo">VapesXperience®</div>
            <ul class="menu-items">
                <li><a href="/">Inicio</a></li>
                <li>
                <a href="https://wa.me/900070749?text=Hola,%20vengo%20por%20información%20de%20Vapes%20al%20x%20mayor" target="_blank">
                 Comprar al x mayor
                     </a>
            </li>


            </ul>
        </nav>
        <div class="carousel-container">
            <div class="carousel">{banners_html}</div>
        </div>
        <div class="products">
            {product_html}
        </div>
        <div class="social-buttons">
            <a href="https://chat.whatsapp.com/IWj2VrmPhn4B8qqov0atAN" target="_blank"><img src="{imgur_images['facebook']}" alt="Facebook"></a>
            <a href="https://www.instagram.com/vapesxperience_peru/#" target="_blank"><img src="{imgur_images['instagram']}" alt="Instagram"></a>
        </div>
        <img src="{imgur_images['whatsapp']}" alt="WhatsApp" class="whatsapp-button" onclick="window.open('https://wa.me/900070749?text=Hola,%20quiero%20más%20información%20sobre%20los%20productos.', '_blank');">
        <script>
            let index = 0;
            function changeBanner() {{
                index = (index + 1) % {len(imgur_images["banners"])};
                document.querySelector('.carousel').style.transform = "translateX(-" + (index * 100 / {len(imgur_images["banners"])}) + "%)";
            }}
            setInterval(changeBanner, 3000);
        
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

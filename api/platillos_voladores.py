from new_restaurant_menu import NewRestaurantMenu


platillos_voladores = NewRestaurantMenu()

# Restaurant

platillos_voladores.create_restaurant(
    name="Platillos Voladores",
    slug="platillos-voladores",
    description="En los últimos años nos hemos concentrado en incluir  sabores de nuestro país y nutrir la carta con investigaciones de platos tradicionales colombianos, interviniendo su presentación o haciendo una fusión con ingredientes del entorno y foráneos.",
    banner="https://firebasestorage.googleapis.com/v0/b/menupp-next.appspot.com/o/images%2Fplatillosvoladores%2Flogos%2Fplatillosvoladores-logo.png?alt=media&token=a99dce02-92af-49fc-8edf-96075793cb00",
)

# Dish Categories

entradas = platillos_voladores.create_dish_category(
    name="Entradas para compartir",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2Fb14b0e36-ec59-4304-8cea-dcfd8e746a87.png?generation=1632337490565757&alt=media",
)

ensaladas = platillos_voladores.create_dish_category(
    name="Ensaladas",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F8dede50e-1097-44e6-973c-61f8b48dce23.png?generation=1632337519865042&alt=media",
)

sopas = platillos_voladores.create_dish_category(
    name="Sopas",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2Fb3e7b94b-6aa5-480c-b379-98bb66b6a565.png?generation=1632337534345761&alt=media",
)

pescados_y_mariscos = platillos_voladores.create_dish_category(
    name="Pescados y Mariscos",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F5fb1d1af-562d-4cce-8629-67ee27ad8928.png?generation=1632337546996707&alt=media",
)

carnes = platillos_voladores.create_dish_category(
    name="Carnes",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F8c6d90a9-a497-428b-9f3f-538b08123e3d.png?generation=1632337557361113&alt=media",
)

aves = platillos_voladores.create_dish_category(
    name="Aves",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F1c200d39-ba33-4104-87f2-0295018b968a.png?generation=1632337568490441&alt=media",
)

wok = platillos_voladores.create_dish_category(
    name="Wok",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F05221f17-2cfb-42f7-8e27-2e16059e0c21.png?generation=1632337579460148&alt=media",
)

postres = platillos_voladores.create_dish_category(
    name="Postres",
    banner="https://storage.googleapis.com/download/storage/v1/b/menupp-next.appspot.com/o/images%2Frestaurants%2Fplatillosvoladores%2F7a9bd2c9-d6c5-442f-a086-f5499e012f37.png?generation=1632337588642489&alt=media",
)

# Badges

disponible_solo_sede_centenario = platillos_voladores.create_badge(
    name="Disponible solo en Sede Centenario",
    type="info",
)

# Dishes

platillos_voladores.create_dish(
    name="Rollitos de Cangrejo y Camarones",
    description="Rollitos rellenos de cangrejo y camarones, sofrito y leche de coco, acompañados de lechuga, cimarrón y mermelada de ají.",
    prices=[
        platillos_voladores.create_price(
            size="6 Unidades",
            final_price=42000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ba51f65f-358d-4355-b56e-2523254f1349.webp",
)

platillos_voladores.create_dish(
    name="Rollitos de Chontaduro",
    description="Rollitos rellenos de chontaduro, queso y mermelada de ají.",
    prices=[
        platillos_voladores.create_price(
            size="6 Unidades",
            final_price=41000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/33272b28-b8cf-4ac2-baab-0c5419377f5f.webp",
)

platillos_voladores.create_dish(
    name="Rollitos de Primavera o Vegetales (Spring Rolls)",
    description="Rollitos rellenos de vegetales, acompañados de lechuga, hierbabuena y salsa de ají dulce.",
    prices=[
        platillos_voladores.create_price(
            size="8 Unidades",
            final_price=39000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/363c4a7a-8e92-438a-8df7-c41dbeae5cdd.webp",
)

platillos_voladores.create_dish(
    name="Lomo Guga",
    description="Trocitos de lomo viche sobre crema de marañones y chipotle, tartar de setas mixtas, acompañado de tostadas de platano.",
    prices=[
        platillos_voladores.create_price(
            final_price=77000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ca7115a6-e68b-45e5-91f3-b4291f1ce7c6.webp",
)

platillos_voladores.create_dish(
    name="Fufú de Camarones",
    description="Montaditos de camarones sobre puré de plátano maduro con sofrito y leche de coco, adornado con chips de plátano.",
    prices=[
        platillos_voladores.create_price(
            final_price=45000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/0b5bb473-5922-4949-b2a3-f7777bcccbcb.webp",
)

platillos_voladores.create_dish(
    name="Carpaccio de Salmón",
    description="Finas laminas de filetes de salmón curado con vinagreta de maracuyá, rugula, queso parmesano, alcachofas y carambolo coronado con arracachas fritas.",
    prices=[
        platillos_voladores.create_price(
            final_price=54000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/5e65a65b-71b8-4190-95f0-f1c2a05f4075.webp",
)

platillos_voladores.create_dish(
    name="Carpaccio de Lomo",
    description="Finas laminas de lomo viche con parmesano, rugula, cebollas crocantes y vinagreta de limoncillo.",
    prices=[
        platillos_voladores.create_price(
            final_price=49000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/f241541f-411b-4454-9b53-f423e0512d59.webp",
)

platillos_voladores.create_dish(
    name="Ceviche Camarones y Mango",
    description="Ceviche inspirado en sabores thailandeses con camarones, mango en julianas, aguacate y champiñones, con vinagreta de limoncillo, salsa de pescado (nampla) y ají.",
    prices=[
        platillos_voladores.create_price(
            final_price=58000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/c818b73f-06ec-4162-835c-294abb4e25cd.webp",
)

platillos_voladores.create_dish(
    name="Ceviche de Pescado y Camarón con Crema de Ají Amarillo",
    description="Ceviche al estilo peruano con Pescado, camarones, cebolla, maíz crocante, crema de ají amarillo y chicharrón de calamar.",
    prices=[
        platillos_voladores.create_price(
            final_price=66000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/a855e837-ac7a-4c2f-90f3-ebf4ea4932dc.webp",
)

platillos_voladores.create_dish(
    name="Ceviche Mixto",
    description="Ceviche inspirado en sabores tailandeses y peruanos con pescado, camarones, pulpo, cebolla, aguacate, tomate fresco, vinagreta de limoncillo y ají.",
    prices=[
        platillos_voladores.create_price(
            final_price=68000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/f1e79dda-7745-4718-ac67-068b86fc7f74.webp",
)

platillos_voladores.create_dish(
    name="Ceviche Mixto con Cremoso de Marañones y Frutos Secos",
    description="Ceviche con Pescado, camarones, pulpo,con crema de marañones y chipotles,cebolla, aguacate, tomate fresco, pistachos, almendras, Vinagreta de limoncillo y ají.Acompañado de palitos de pan árabe tostados.",
    prices=[
        platillos_voladores.create_price(
            final_price=75000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/34ca3054-8708-4365-b041-49c8b691878b.webp",
)

platillos_voladores.create_dish(
    name="Ceviche con Cremoso de Marañones y Frutos Secos",
    description="Ceviche de pescado fresco con crema de marañones y chipotles acompañado de palitos de pan arabe tostados",
    prices=[
        platillos_voladores.create_price(
            final_price=75000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/34ca3054-8708-4365-b041-49c8b691878b.webp",
)

platillos_voladores.create_dish(
    name="Chicharrón Acevichado",
    description="Chicharrón crocante, con escabeche cebolla y ají fresco, aguacate,tomate, crema de ají amarillo y trozos de naranja, acompañado de frituras mixtas.",
    prices=[
        platillos_voladores.create_price(
            final_price=65000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/d8bceca8-4ed9-45b9-bc73-7220bb4f78cb.webp",
)

platillos_voladores.create_dish(
    name="Chuleta & Chips",
    description="Chuleticas de res, acompañado de papas rusticas y salsa de tomate o chipotle ",
    prices=[
        platillos_voladores.create_price(
            final_price=35000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/4530c5cc-c07b-4cdd-8881-ce518ea87aee.webp",
)

platillos_voladores.create_dish(
    name="Carapachos De Cangrejo y Camarones",
    description="Carapachos rellenos de cangrejo y camarones, sofrito y leche de coco.",
    prices=[
        platillos_voladores.create_price(
            final_price=57000,
        ).id
    ],
    categories=[entradas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/051ae05b-d329-4098-84fe-863138a70b57.webp",
)

platillos_voladores.create_dish(
    name="Ceviche de Pescado Fresco",
    description="Pescado fresco, cebolla, aguacate, ají dulce, maíz, tomate fresco, vinagreta de limoncillo y ají, acompañado de frituras.",
    prices=[
        platillos_voladores.create_price(
            final_price=68000,
        ).id
    ],
    categories=[entradas],
)

platillos_voladores.create_dish(
    name="Ensalada Quinua y Pollo",
    description="Quinua, Pollo, lechugas mixtas, espinacas, tomate cherry, maíz crocante, almendras, vinagreta de maracuyá y gomasio.",
    prices=[
        platillos_voladores.create_price(
            final_price=44000,
        ).id
    ],
    categories=[ensaladas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ad8617e9-bf1a-4424-8009-17a9eea122ef.webp",
)

platillos_voladores.create_dish(
    name="Ensalada Carpaccio de Lomo",
    description="Finas laminas de lomo viche, vinagreta de limoncillo, lechugas mixtas, champiñones, pimentones asados, tomates secos, queso parmesano y coronado con cebollas crocantes.",
    prices=[
        platillos_voladores.create_price(
            final_price=53000,
        ).id
    ],
    categories=[ensaladas],
    recommended=True,
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/476bac25-bf33-4448-9f46-02dbaa3f04b4.webp",
)

platillos_voladores.create_dish(
    name="Ensalada de Pollo",
    description="Pollo, mozarella de búfala, lechugas mixtas, espinacas, champiñones, tomate fresco, pimentones asados, maíz tierno, aceitunas, vinagreta de mostaza y gomasio.",
    prices=[
        platillos_voladores.create_price(
            final_price=48000,
        ).id
    ],
    categories=[ensaladas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/16662188-6c88-4964-a1e5-77672c46b2c3.webp",
)

platillos_voladores.create_dish(
    name="Ensalada de Camarones",
    description="Camarones, lechugas mixtas, champiñones, tomate cherry, mango, aguacate, espinacas, vinagreta de limoncillo, salsa de pescado (nampla), gomasio y cebolla frita.",
    prices=[
        platillos_voladores.create_price(
            final_price=60000,
        ).id
    ],
    categories=[ensaladas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/a2a0a517-f59e-4288-9383-dd7c6c677cf6.webp",
)

platillos_voladores.create_dish(
    name="Sopa Baudó",
    description="Tradicional sopa del Pacífico colombiano de pasta con queso criollo, camarones, sofrito y leche de coco.",
    prices=[
        platillos_voladores.create_price(
            size="Mediana",
            final_price=44000,
        ).id,
        platillos_voladores.create_price(
            size="Grande",
            final_price=49000,
        ).id,
    ],
    recommended=True,
    categories=[sopas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/302ba990-2baf-4917-94e6-a028e0485225.webp",
)

platillos_voladores.create_dish(
    name="Sopa Baudó de Tofu",
    description="Sopa vegetariana de tofu, sofrito, pasta, queso criollo y leche de coco. (Opción vegana sin queso).",
    prices=[
        platillos_voladores.create_price(
            size="Mediana",
            final_price=34000,
        ).id,
        platillos_voladores.create_price(
            size="Grande",
            final_price=38000,
        ).id,
    ],
    categories=[sopas],
)

platillos_voladores.create_dish(
    name="Sopa de Tomate",
    description="Salsa napolitana, tomates frescos, ajo, queso parmesano, crocantes de pan árabe y albahaca",
    prices=[
        platillos_voladores.create_price(
            size="Mediana",
            final_price=32000,
        ).id,
        platillos_voladores.create_price(
            size="Grande",
            final_price=38000,
        ).id,
    ],
    categories=[sopas],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/a95b459d-8549-4966-aecc-7923525f4d4a.webp",
)

platillos_voladores.create_dish(
    name="Sopa Tom Yum",
    description="Sopa tailandesa de camarones, fondo de pescado, cebolla , calabacín amarillo y verde, ají, jengibre, salsa de pescado (nampla) y leche de coco.",
    prices=[
        platillos_voladores.create_price(
            size="Mediana",
            final_price=45000,
        ).id,
        platillos_voladores.create_price(
            size="Grande",
            final_price=55000,
        ).id,
    ],
    categories=[sopas],
)

platillos_voladores.create_dish(
    name="Encocado de Pescado y Camarones",
    description="Cazuela de pescado y camarones con sofrito y leche de coco, acompañado de arroz blanco.",
    prices=[
        platillos_voladores.create_price(
            final_price=80000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    recommended=True,
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/c1dcefbc-2d2e-40d3-ad76-8b245e125946.webp",
)

platillos_voladores.create_dish(
    name="Encocado De Camarones",
    description="Cazuela de camarones con sofrito y leche de coco, acompañado de arroz blanco.",
    prices=[
        platillos_voladores.create_price(
            final_price=78000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/68d69eb0-6f3d-4573-a9d0-d7eaad524237.webp",
)

platillos_voladores.create_dish(
    name="Pescado Primavera",
    description="Filete de pescado fresco en reducción de vino blanco, tomates frescos y secos, aceite de oliva coronado con una ensalada de lechugas mixtas, alcaparras fritas.",
    prices=[
        platillos_voladores.create_price(
            final_price=78000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/d251f395-d6ed-4270-8ecc-9d3f523e975b.webp",
)

platillos_voladores.create_dish(
    name="Pescado Chontaduro",
    description="Filete de pescado fresco en reducción de vino blanco con salsa de chontaduro y mermelada de ají sobre puré de papa amarilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=75000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/c57d813e-1c06-4164-83ef-1619714d86a1.webp",
)

platillos_voladores.create_dish(
    name="Pescado Krishnaizza",
    description="Filete de pescado fresco en reducción de vino blanco, curry rojo y crema de coco, sobre vegetales salteados y coronado con camarones al wok y cebollas crocantes.",
    prices=[
        platillos_voladores.create_price(
            final_price=80000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ac144a26-232c-4b5c-8d4d-cfdc993e4aa8.webp",
)

platillos_voladores.create_dish(
    name="Salmón Macadamia",
    description="Filete de Salmón con mantequilla de macadamia y cebollas caramelizadas, sobre puré de papa amarilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=75000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/5157f03f-42e5-4588-9389-6dca050046c8.webp",
)

platillos_voladores.create_dish(
    name="Salmón Maracuyá",
    description="Filete de Salmón con salsa de maracuyá, sobre puré de papa amarilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=70000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ee6c7ec3-b849-404b-acbb-2f6c3174ab3b.webp",
)


platillos_voladores.create_dish(
    name="Pescado Pacífico",
    description="Filete de pescado fresco con sofrito y leche de coco, puré de plátano maduro y coronado con camarones.",
    prices=[
        platillos_voladores.create_price(
            final_price=80000,
        ).id
    ],
    categories=[pescados_y_mariscos],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/fed0db48-1a58-4619-9718-546b7440233f.webp",
)

platillos_voladores.create_dish(
    name="Pescado Camarón Curry Rojo",
    description="Trozos de pescado fresco y camarones con vegetales al wok en salsa de curry rojo y leche de coco al estilo Thai.",
    prices=[
        platillos_voladores.create_price(
            final_price=78000,
        ).id
    ],
    categories=[pescados_y_mariscos],
)

platillos_voladores.create_dish(
    name="Costilla Nikkei",
    description="Costilla de cerdo cocinada lentamente al vacío y glaseada en salsa soya japonesa, hondashi, jengibre y azúcar sobre cremoso de yuca.",
    prices=[
        platillos_voladores.create_price(
            final_price=60000,
        ).id
    ],
    categories=[carnes],
    recommended=True,
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/5db015fa-4ae1-4933-a75b-5712a331b2cc.webp",
)

platillos_voladores.create_dish(
    name="Lomo Quevedo",
    description="Medallón de lomo viche bañado en reducción de demi-glace, pimienta negra y vino tinto, con cebollas crocantes y acompañado de espagueti a la crema. ",
    prices=[
        platillos_voladores.create_price(
            final_price=65000,
        ).id
    ],
    categories=[carnes],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/b998aee9-6aaf-4310-9117-5726a421f34d.webp",
)


platillos_voladores.create_dish(
    name="Posta Negra",
    description="Punta de anca marinada en hierbas, cocida lentamente al vacío con salsa negra y panela, sobre vegetales, acompañada con arroz con coco y cebollas crocantes.",
    prices=[
        platillos_voladores.create_price(
            final_price=65000,
        ).id
    ],
    categories=[carnes],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/76747fa8-06ac-4f0b-9701-611aa57780b8.webp",
)


platillos_voladores.create_dish(
    name="Lomo Yin Yang",
    description="Plato mixto de medallón de lomo con champiñones y salsa de queso azul y medallón de lomo con salsa de tres pimientas y cebolla frita.",
    prices=[
        platillos_voladores.create_price(
            final_price=77000,
        ).id
    ],
    categories=[carnes],
    recommended=True,
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/0e0f6717-101f-4647-87c6-8a4a04d5052a.webp",
)


platillos_voladores.create_dish(
    name="Lomo Pacífico",
    description="Medallones de Lomo viche con sofrito, leche de coco y camarones crocantes, acompañado de puré de platano maduro y chips de platano.",
    prices=[
        platillos_voladores.create_price(
            final_price=80000,
        ).id
    ],
    categories=[carnes],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/61ca2a71-3ada-41b6-b24a-eb1ee2fb1c4e.webp",
)


platillos_voladores.create_dish(
    name="Lomo Hierbabuena y Pimienta",
    description="Tagliata de Lomito viche encostrado en hierbabuena y pimienta, con vinagreta de limoncillo, salsa de pescado (nam pla), ají y cebollas crocantes, acompañado de arroz albahaca.",
    prices=[
        platillos_voladores.create_price(
            final_price=65000,
        ).id
    ],
    categories=[carnes],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/335945ef-8d5c-421d-b7ee-6e92f6a0478e.webp",
)


platillos_voladores.create_dish(
    name="Lomo Vallejo",
    description="Plato mixto de medallón de lomo con champiñones y salsa de queso azul y medallón de lomo con bananitos acaramelados en amaretto, acompañado de ensalada.",
    prices=[
        platillos_voladores.create_price(
            final_price=76000,
        ).id
    ],
    categories=[carnes],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/dd092a32-1e89-47d9-a906-2eedb3c1b5cb.webp",
)


platillos_voladores.create_dish(
    name="Pollo Pacífico ",
    description="Pechuga de pollo, sofrito, leche de coco y camarones crocantes, acompañado de puré de plátano maduro.",
    prices=[
        platillos_voladores.create_price(
            final_price=56000,
        ).id
    ],
    categories=[aves],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/731cb60a-7566-4493-a1a3-fbc11bac8ec4.webp",
)


platillos_voladores.create_dish(
    name="Pollo Guayaba",
    description="Rollos de pollo con ricotta y dulce de guayaba en salsa de queso azul, acompañado de puré de papa amarilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=55000,
        ).id
    ],
    categories=[aves],
    recommended=True,
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/1e44a4b9-bbfa-4a93-940c-c97ec1524712.webp",
)


platillos_voladores.create_dish(
    name="Pollo al Curry Verde",
    description="Trocitos de pollo con vegetales al wok, pasta de curry verde y leche de coco, acompañado de arroz blanco.",
    prices=[
        platillos_voladores.create_price(
            final_price=46000,
        ).id
    ],
    categories=[aves],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/8747f13f-7286-48c7-9d65-14afedb87eda.webp",
)


platillos_voladores.create_dish(
    name="Pollo Pimienta",
    description="Pechuga de pollo, con champiñones frescos, salsa de pimienta y espagueti al burro.",
    prices=[
        platillos_voladores.create_price(
            final_price=48000,
        ).id
    ],
    categories=[aves],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/10e82251-0981-431c-b67c-8205f409f14d.webp",
)


platillos_voladores.create_dish(
    name="Arroz Thai",
    description="Arroz al estilo oriental con camarones, pollo, cerdo, vegetales, maíz, manzana, salsa de pescado, salsa de ostras y salsa de soya",
    prices=[
        platillos_voladores.create_price(
            final_price=50000,
        ).id
    ],
    categories=[wok],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/4a248f7d-dba1-4a79-8b7e-30c38929b196.webp",
)


platillos_voladores.create_dish(
    name="Arroz Yaffi",
    description="Arroz frito con vegetales, cinco especias chinas, maní, almendras, salsas de ostras, nampla y soya (puede ordenar este plato totalmente, vegetariano con solo soya). ",
    prices=[
        platillos_voladores.create_price(
            final_price=30000,
        ).id
    ],
    categories=[wok],
)


platillos_voladores.create_dish(
    name="Risotto Pacífico",
    description="Arroz arbóreo, camarones, calamares, cangrejo, mejillones, sofrito, leche de coco y parmesano.",
    prices=[
        platillos_voladores.create_price(
            final_price=80000,
        ).id
    ],
    badges=[disponible_solo_sede_centenario],
    categories=[wok],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/246959ca-5c13-4fd9-9e35-8f0a7beb8941.webp",
)


platillos_voladores.create_dish(
    name="Risotto de Vegetales y Champiñones",
    description="Arroz arbóreo con vegetales, tomates secos y frescos, albahaca, perejil, hongos portobello,  champiñones, queso azul y parmesano.",
    prices=[
        platillos_voladores.create_price(
            final_price=65000,
        ).id
    ],
    categories=[wok],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/ff0ea25c-57ab-485a-96dd-bdf5a4919987.webp",
)


platillos_voladores.create_dish(
    name="Quinua al wok",
    description="Quinua salteada con cebolla, pimentón, pistachos, almendras, aceite de oliva y torre de vegetales : portobello, tomate y calabacín, bañados en salsa pesto de albahaca, sobre puré de plátano maduro.",
    prices=[
        platillos_voladores.create_price(
            final_price=45000,
        ).id
    ],
    categories=[wok],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/72d8a003-36a0-4b45-80ce-dbe38efe41fc.webp",
)


platillos_voladores.create_dish(
    name="Tofu al Curry Verde",
    description="Trocitos de tofu y vegetales al wok en salsa de curry verde y leche de coco acompañado de arroz blanco.",
    prices=[
        platillos_voladores.create_price(
            final_price=42000,
        ).id
    ],
    categories=[wok],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/0a5e1c0e-da07-4c5e-8244-b7da9211ffbc.webp",
)


platillos_voladores.create_dish(
    name="Flan de Caramelo",
    description="Flan de leche con salsa de caramelo.",
    prices=[
        platillos_voladores.create_price(
            final_price=15000,
        ).id
    ],
    categories=[postres],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/0c645dcf-1677-4c34-b038-77d69bc70c90.webp",
)


platillos_voladores.create_dish(
    name="Merengado",
    description="Merengue o suspiro, crema chantilly, coulis de mora, coulis de lulo con  trozos de lulo, piña uchuvas, moras, maracuya y hierbabuena. ",
    prices=[
        platillos_voladores.create_price(
            final_price=25000,
        ).id
    ],
    categories=[postres],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/482b977a-e12c-4896-b18e-8e688bd8e4bb.webp",
)


platillos_voladores.create_dish(
    name="Turrón Crocante ",
    description="Crocante de galleta de chocolate triturado, almendras tostadas y coco deshidratado, con helado de vainilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=28000,
        ).id
    ],
    categories=[postres],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/7457ba6e-8193-42d6-81cc-cdeacc891a01.webp",
)


platillos_voladores.create_dish(
    name="Bananitos Crocantes",
    description="Rollitos rellenos de banano con azúcar pulverizada y salsa de chocolate, acompañados con helado de vainilla.",
    prices=[
        platillos_voladores.create_price(
            final_price=18000,
        ).id
    ],
    categories=[postres],
    main_image="https://dvzwo3mu4ucsq.cloudfront.net/images/restaurants/platillosvoladores/67a6715d-d4d2-42a7-949b-8266fa796460.webp",
)

platillos_voladores.create_menu(
    slug="platillos-voladores",
    name="platillos-voladores",
)

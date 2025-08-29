import streamlit as st
import pandas as pd

st.set_page_config(page_title="Revisión de Contenidos Kar & Ma", layout="wide")

st.title("📝 Revisión de Contenidos")
st.write("Por favor, revisa cada bloque de texto actual y escribe el reemplazo correspondiente.")

textos = {
    "Header - Menú": "Logo | Inicio | Nosotros | Submarcas | Segmentos | Clientes | Cotización",

    "Hero - Título": "Excelencia en sal retail e industrial awdas",
    "Hero - Subtítulo": "Consorcio con más de 30 años de experiencia produciendo sal para empresas e industria local",

    "Historia - Título": "Historia del Grupo Kar & Ma",
    "Historia - Texto": """Durante más de tres décadas, Kar & Ma S.A.C. ha sido un pilar fundamental en la industria salinera peruana. 
Nacimos en el norte del país con la visión de proporcionar sal de la más alta calidad tanto para el consumo retail como para las grandes industrias nacionales.

Nuestro compromiso con la excelencia nos ha permitido expandirnos y consolidarnos como un consorcio de confianza, 
respaldado por la tradición y el trabajo del pueblo del norte peruano.""",

    "Misión": "Proveer sal de excelente calidad para el mercado retail e industrial, manteniendo los más altos estándares de producción y servicio al cliente.",
    "Visión": "Ser el consorcio salinero líder en el Perú, reconocido por nuestra calidad, innovación y compromiso con el desarrollo sostenible.",
    "Valores": "Calidad: En cada proceso\nConfianza: En cada relación\nInnovación: En cada solución",

    "Trayectoria": """1990s – Fundación del grupo en el norte del Perú
2000s – Expansión de operaciones y desarrollo de submarcas
2010s – Consolidación en el mercado industrial y retail
2020s – Liderazgo nacional y reconocimiento del mercado""",

    "Submarcas - Intro": "Marcas consolidadas dentro del consorcio Kar & Ma",
    "Submarca - Salina": "Nuestra marca premium enfocada en productos de sal de alta calidad para el mercado retail y gastronómico. Reconocida por su pureza y presentación excepcional que satisface los estándares más exigentes.",
    "Submarca - Norteñita": "La marca que representa nuestras raíces norteñas, especializada en sal tradicional para el hogar peruano. Conecta con la cultura local y mantiene la esencia de nuestros orígenes en cada producto.",
    "Submarcas - Nota": "Ambas submarcas mantienen los altos estándares de calidad que caracterizan al consorcio Kar & Ma, adaptándose a las necesidades específicas de cada segmento del mercado.",

    "Segmentos - Intro": "Dos líneas de negocio especializadas para atender diferentes mercados",
    "Segmento - Retail": """Dirigido al consumo doméstico y comercial pequeño. Ofrecemos productos de sal refinada, sal marina y especialidades gastronómicas en presentaciones adaptadas para el hogar, restaurantes y pequeños negocios.
Productos incluidos:
• Sal de mesa refinada
• Sal marina natural
• Sal yodada
• Especialidades gastronómicas""",
    "Segmento - Industrial": """Soluciones especializadas para grandes empresas y sectores industriales. Suministramos sal técnica, sal para procesamiento de alimentos, conservación y aplicaciones industriales específicas.
Sectores atendidos:
• Industria alimentaria
• Sector pesquero
• Industria agrícola
• Procesos industriales""",

    "Clientes - Intro": "\"La confianza del pueblo del norte nos respalda\"\nOrgullosamente Norteños\nTradición y calidad desde el corazón del norte peruano",
    "Clientes - Empresas": "Cliente 1 | Cliente 2 | Cliente 3 | Cliente 4 | Cliente 5 | Cliente 6 | Cliente 7 | Cliente 8 (Se debe reemplazar cliente X por el nombre de los clientes)",
    "Testimonio - Cliente 1": "\"Kar & Ma ha sido nuestro proveedor de sal industrial por más de 15 años...\" – Empresa Pesquera del Norte (Sector Pesquero)",
    "Testimonio - Cliente 2": "\"La calidad de sus productos retail bajo la marca Norteñita es excepcional...\" – Distribuidora Regional (Comercio Retail)",
    "Testimonio - Cliente 3": "\"Kar & Ma ha sido nuestro proveedor de sal industrial por más de 15 años...\" – Empresa Pesquera del Norte (Sector Pesquero)",
    "Testimonio - Cliente 4": "\"La calidad de sus productos retail bajo la marca Norteñita es excepcional...\" – Distribuidora Regional (Comercio Retail)",
    "Testimonio - Cliente 5": "\"Kar & Ma ha sido nuestro proveedor de sal industrial por más de 15 años...\" – Empresa Pesquera del Norte (Sector Pesquero)",
    "Testimonio - Cliente 6": "\"La calidad de sus productos retail bajo la marca Norteñita es excepcional...\" – Distribuidora Regional (Comercio Retail)",
    "Testimonio - Cliente 7": "\"Kar & Ma ha sido nuestro proveedor de sal industrial por más de 15 años...\" – Empresa Pesquera del Norte (Sector Pesquero)",
    "Testimonio - Cliente 8": "\"La calidad de sus productos retail bajo la marca Norteñita es excepcional...\" – Distribuidora Regional (Comercio Retail)",
    "Clientes - Nota": "Más de 300 empresas del norte del Perú confían en nuestros productos y servicios, desde pequeños negocios familiares hasta grandes corporaciones industriales.",

    "Contacto - Intro": "Conecta con nosotros para soluciones empresariales en sal",
    "Contacto - Formulario": "Formulario Empresarial: Nombre * | Empresa * | Email * | Mensaje * (Especificar si secesitan quitar algun campo o agregar un dato mas, tal como RUC, telefono, etc)",
    "Ubicación": "Planta Industrial – Región Norte del Perú, Zona Industrial Salinera",
    "Email": "contacto@karma.com.pe",
    "Teléfono": "+51 999 999 999",
    "WhatsApp": "Para consultas rápidas de precios y disponibilidad",
    "Footer": "© 2025 Kar & Ma. Todos los derechos reservados. Tradición salinera del norte peruano.",
}

reemplazos = {}

st.subheader("Formulario")
for clave, valor in textos.items():
    with st.expander(clave, expanded=False):
        st.write("**Texto actual:**")
        st.info(valor)
        reemplazos[clave] = st.text_area(f"Nuevo texto para '{clave}'", "")


if st.button("💾 Guardar en Excel"):
    df = pd.DataFrame(list(reemplazos.items()), columns=["Sección", "Reemplazo"])
    df.to_excel("reemplazos.xlsx", index=False)
    st.success("Archivo 'reemplazos.xlsx' generado correctamente.")
    st.download_button("⬇️ Descargar Excel", df.to_csv(index=False).encode("utf-8"), "reemplazos.csv", "text/csv")

"""
Script to populate the database with initial videos and testimonials
Run this after creating the database tables with: flask db upgrade
"""

from app import create_app, db
from app.models import Video, Testimonial


def populate_videos():
    """Add initial videos to the database"""
    videos_data = [
        {
            "title": "Deportivo - Audi A4",
            "description": "Producción cinematográfica de vehículos con perspectivas aéreas dinámicas",
            "filename": "Deportivo.mp4",
            "category": "Deportivo",
            "order": 0,
        },
        {
            "title": "Naturaleza - Life Moments",
            "description": "Capturando la esencia de la vida desde el cielo con narrativa visual",
            "filename": "Naturaleza.mp4",
            "category": "Naturaleza",
            "order": 1,
        },
        {
            "title": "Carrera - Motorbike Action",
            "description": "Acción y velocidad capturadas con tomas aéreas de alta energía",
            "filename": "Carrera.mp4",
            "category": "Carrera",
            "order": 2,
        },
    ]

    for video_data in videos_data:
        # Check if video already exists
        existing = Video.query.filter_by(filename=video_data["filename"]).first()
        if not existing:
            video = Video(**video_data)
            db.session.add(video)
            print(f"Added video: {video_data['title']}")
        else:
            print(f"Video already exists: {video_data['title']}")

    db.session.commit()


def populate_testimonials():
    """Add initial testimonials to the database"""
    testimonials_data = [
        {
            "author_name": "María García",
            "author_role": "Cliente Bodas",
            "author_image_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "UpFrames capturó nuestra boda de manera espectacular. Las tomas aéreas añadieron una perspectiva única e inolvidable.",
            "order": 0,
        },
        {
            "author_name": "Carlos Ruiz",
            "author_role": "Evento Corporativo",
            "author_image_url": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "El profesionalismo y la calidad de sus videos superaron nuestras expectativas. Altamente recomendados.",
            "order": 1,
        },
        {
            "author_name": "Ana Martínez",
            "author_role": "Agencia Inmobiliaria",
            "author_image_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "Trabajo excepcional. Los videos aéreos de nuestra propiedad ayudaron a venderla en tiempo récord.",
            "order": 2,
        },
        {
            "author_name": "Jorge López",
            "author_role": "Director de Marketing",
            "author_image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "La creatividad y atención al detalle son impresionantes. Cada toma cuenta una historia.",
            "order": 3,
        },
        {
            "author_name": "Laura Fernández",
            "author_role": "Organizadora de Eventos",
            "author_image_url": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "Transformaron nuestro evento en un recuerdo cinematográfico. Increíble trabajo técnico y artístico.",
            "order": 4,
        },
        {
            "author_name": "David Sánchez",
            "author_role": "Empresario",
            "author_image_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=150&h=150",
            "content": "El video promocional de mi negocio ha generado un impacto increíble. Completamente satisfecho.",
            "order": 5,
        },
    ]

    for testimonial_data in testimonials_data:
        # Check if testimonial already exists
        existing = Testimonial.query.filter_by(
            author_name=testimonial_data["author_name"]
        ).first()
        if not existing:
            testimonial = Testimonial(**testimonial_data)
            db.session.add(testimonial)
            print(f"Added testimonial: {testimonial_data['author_name']}")
        else:
            print(f"Testimonial already exists: {testimonial_data['author_name']}")

    db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        print("\nPopulating database...")
        print("\nAdding videos...")
        populate_videos()
        print("\nAdding testimonials...")
        populate_testimonials()
        print("\nDatabase populated successfully!\n")

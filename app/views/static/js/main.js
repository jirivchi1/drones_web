document.addEventListener('DOMContentLoaded', function() {
    // Video de fondo principal - Reducir velocidad y optimizar calidad
    const heroVideo = document.querySelector('.hero-video');
    if (heroVideo) {
        heroVideo.playbackRate = 0.75; // 75% de velocidad (más lento)

        // Forzar al navegador a usar la máxima calidad disponible
        heroVideo.addEventListener('loadedmetadata', function() {
            // Obtener las pistas de video disponibles
            const videoTracks = heroVideo.videoTracks;
            if (videoTracks && videoTracks.length > 0) {
                // Seleccionar la pista de mayor calidad
                for (let i = 0; i < videoTracks.length; i++) {
                    videoTracks[i].selected = (i === videoTracks.length - 1);
                }
            }
        });
    }

    // Rotación de palabras en el hero
    const words = document.querySelectorAll('.dynamic-word');

    if (words.length > 0) {
        let currentIndex = 0;

        function rotateWords() {
            const currentWord = words[currentIndex];
            currentWord.classList.remove('active');
            currentWord.classList.add('exit');

            setTimeout(() => {
                currentWord.classList.remove('exit');
            }, 500);

            currentIndex = (currentIndex + 1) % words.length;

            const nextWord = words[currentIndex];
            nextWord.classList.add('active');
        }

        setInterval(rotateWords, 2500);
    }

    // Carrusel de videos con botones de categoría
    const track = document.getElementById('carouselTrack');
    const categoryBtns = document.querySelectorAll('.category-btn');

    if (!track || categoryBtns.length === 0) return;

    let currentSlide = 0;
    const totalSlides = document.querySelectorAll('.carousel-item').length;

    function updateCarousel() {
        const itemWidth = track.querySelector('.carousel-item').offsetWidth;
        const gap = 32;
        const offset = currentSlide * (itemWidth + gap);

        track.style.transform = `translateX(-${offset}px)`;

        // Actualizar botones activos
        categoryBtns.forEach((btn, index) => {
            btn.classList.toggle('active', index === currentSlide);
        });
    }

    // Click en botones de categoría
    categoryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const categoryIndex = parseInt(btn.dataset.category);

            // Pausar video actual si está reproduciéndose
            const currentVideo = document.querySelectorAll('.video-wrapper')[currentSlide];
            if (currentVideo) {
                const video = currentVideo.querySelector('video');
                if (video && !video.paused) {
                    video.pause();
                    currentVideo.classList.remove('playing');
                }
            }

            // Cambiar a nuevo video
            currentSlide = categoryIndex;
            updateCarousel();

            // Reproducir automáticamente el nuevo video
            setTimeout(() => {
                const newVideoWrapper = document.querySelectorAll('.video-wrapper')[currentSlide];
                if (newVideoWrapper) {
                    const newVideo = newVideoWrapper.querySelector('video');
                    if (newVideo) {
                        newVideo.play();
                        newVideoWrapper.classList.add('playing');
                    }
                }
            }, 600); // Esperar a que termine la animación del carrusel
        });
    });

    window.addEventListener('resize', updateCarousel);

    updateCarousel();

    // Video players - Click para reproducir/pausar
    const videoWrappers = document.querySelectorAll('.video-wrapper');

    videoWrappers.forEach(wrapper => {
        const video = wrapper.querySelector('video');
        const playButton = wrapper.querySelector('.play-button');

        wrapper.addEventListener('click', (e) => {
            if (!wrapper.classList.contains('playing')) {
                // Pausar todos los otros videos
                videoWrappers.forEach(w => {
                    const v = w.querySelector('video');
                    if (v !== video) {
                        v.pause();
                        w.classList.remove('playing');
                    }
                });

                // Reproducir este video
                video.play();
                wrapper.classList.add('playing');
            } else {
                // Pausar el video si está reproduciéndose
                video.pause();
            }
        });

        // Cuando el video se pausa, mostrar el botón de play
        video.addEventListener('pause', () => {
            wrapper.classList.remove('playing');
        });

        // Cuando el video termina, mostrar el botón de play
        video.addEventListener('ended', () => {
            wrapper.classList.remove('playing');
        });
    });

    // Testimonios - Duplicar contenido para scroll infinito
    const columns = document.querySelectorAll('.testimonials-column');

    columns.forEach(column => {
        const cards = column.querySelectorAll('.testimonial-card');
        cards.forEach(card => {
            const clone = card.cloneNode(true);
            column.appendChild(clone);
        });
    });

    console.log('UpFrames - App cargada correctamente');
});

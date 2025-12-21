document.addEventListener('DOMContentLoaded', function() {
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

    // Carrusel de videos
    const track = document.getElementById('carouselTrack');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const indicators = document.querySelectorAll('.indicator');

    if (!track || !prevBtn || !nextBtn) return;

    let currentSlide = 0;
    const totalSlides = document.querySelectorAll('.carousel-item').length;

    function updateCarousel() {
        const itemWidth = track.querySelector('.carousel-item').offsetWidth;
        const gap = 32;
        const offset = currentSlide * (itemWidth + gap);

        track.style.transform = `translateX(-${offset}px)`;

        prevBtn.disabled = currentSlide === 0;
        nextBtn.disabled = currentSlide >= totalSlides - 1;

        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentSlide);
        });
    }

    prevBtn.addEventListener('click', () => {
        if (currentSlide > 0) {
            currentSlide--;
            updateCarousel();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentSlide < totalSlides - 1) {
            currentSlide++;
            updateCarousel();
        }
    });

    indicators.forEach(indicator => {
        indicator.addEventListener('click', () => {
            currentSlide = parseInt(indicator.dataset.index);
            updateCarousel();
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

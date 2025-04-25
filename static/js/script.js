const destacados = JSON.parse('{{ destacados | tojson | safe }}');
    
        // Crear iframes dinámicamente usando el enlace embebido
        destacados.forEach(video => {
            const container = document.querySelector('.container-videos-destacados');
            const iframe = document.createElement('iframe');
            iframe.width = "560";
            iframe.height = "315";
            iframe.src = video.embed_link;  // Usa el enlace embebido directamente
            iframe.frameBorder = "0";
            iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
            iframe.allowFullscreen = true;
    
            const videoContainer = document.createElement('div');
            videoContainer.appendChild(iframe);
            container.appendChild(videoContainer);
        });
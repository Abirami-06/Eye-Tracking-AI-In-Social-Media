document.addEventListener('DOMContentLoaded', function () {
    const posts = document.querySelectorAll('.feed li');
    let activePost = null;

    window.addEventListener('scroll', () => {
        let closestPost = null;
        let minDistance = Infinity;

        posts.forEach(post => {
            const rect = post.getBoundingClientRect();
            const distance = Math.abs(rect.top - window.innerHeight / 2);

            if (distance < minDistance) {
                minDistance = distance;
                closestPost = post;
            }
        });

        if (closestPost && activePost !== closestPost) {
            if (activePost) activePost.classList.remove('highlight');
            closestPost.classList.add('highlight');
            activePost = closestPost;
        }
    });
});

// --- Mobile Menu Toggle ---
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuToggle.classList.toggle('is-active');

        // Transform hamburger to X
        const bars = menuToggle.querySelectorAll('.bar');
        bars[0].style.transform = navLinks.classList.contains('active') ? 'rotate(45deg) translate(5px, 6px)' : 'none';
        bars[1].style.opacity = navLinks.classList.contains('active') ? '0' : '1';
        bars[2].style.transform = navLinks.classList.contains('active') ? 'rotate(-45deg) translate(5px, -6px)' : 'none';
    });
}

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        // Reset hamburger
        const bars = menuToggle.querySelectorAll('.bar');
        bars.forEach(bar => bar.style.transform = 'none');
        bars[1].style.opacity = '1';
    });
});

// --- Scroll Reveal Animation ---
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
}, observerOptions);

const scrollElements = document.querySelectorAll('.scroll-animate');
scrollElements.forEach(el => observer.observe(el));

// --- Navbar Background Change on Scroll ---
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.padding = '0.8rem 0';
        navbar.style.background = 'rgba(7, 11, 20, 0.95)';
    } else {
        navbar.style.padding = '1.2rem 0';
        navbar.style.background = 'rgba(7, 11, 20, 0.85)';
    }
});

// --- Active Link on Scroll ---
const sections = document.querySelectorAll('section, header');
const navItems = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href').includes(current)) {
            item.classList.add('active');
            item.style.color = 'var(--accent)';
        } else {
            item.style.color = 'var(--text-muted)';
        }
    });
});

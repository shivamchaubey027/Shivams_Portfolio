// Main JavaScript file for portfolio website
(function() {
    'use strict';

    // Mobile Navigation Toggle
    function initMobileNav() {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');
        
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
                
                // Animate hamburger menu
                const bars = navToggle.querySelectorAll('.bar');
                bars.forEach(bar => bar.classList.toggle('active'));
            });

            // Close mobile menu when clicking on a link
            const navLinks = navMenu.querySelectorAll('.nav-link');
            navLinks.forEach(function(link) {
                link.addEventListener('click', function() {
                    navMenu.classList.remove('active');
                    const bars = navToggle.querySelectorAll('.bar');
                    bars.forEach(bar => bar.classList.remove('active'));
                });
            });

            // Close mobile menu when clicking outside
            document.addEventListener('click', function(event) {
                if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                    navMenu.classList.remove('active');
                    const bars = navToggle.querySelectorAll('.bar');
                    bars.forEach(bar => bar.classList.remove('active'));
                }
            });
        }
    }

    // Smooth scrolling for anchor links
    function initSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const headerOffset = 80;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // Add scroll effect to navbar
    function initNavbarScroll() {
        const navbar = document.querySelector('.navbar');
        
        if (navbar) {
            let lastScrollTop = 0;
            let scrollTimeout;

            window.addEventListener('scroll', function() {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                
                // Add shadow when scrolled
                if (scrollTop > 10) {
                    navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
                } else {
                    navbar.style.boxShadow = 'none';
                }

                // Hide/show navbar on scroll (optional)
                if (scrollTop > lastScrollTop && scrollTop > 100) {
                    // Scrolling down
                    navbar.style.transform = 'translateY(-100%)';
                } else {
                    // Scrolling up
                    navbar.style.transform = 'translateY(0)';
                }
                
                lastScrollTop = scrollTop;
                
                // Clear timeout and set a new one
                clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(function() {
                    navbar.style.transform = 'translateY(0)';
                }, 200);
            });
        }
    }

    // Lazy loading for images
    function initLazyLoading() {
        const images = document.querySelectorAll('img[loading="lazy"]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.classList.add('fade-in');
                        observer.unobserve(img);
                    }
                });
            });

            images.forEach(function(img) {
                imageObserver.observe(img);
            });
        }
    }

    // Form handling
    function initFormHandling() {
        const contactForm = document.querySelector('.contact-form-container');
        
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                // Add loading state
                const submitButton = contactForm.querySelector('button[type="submit"]');
                const originalText = submitButton.innerHTML;
                
                submitButton.innerHTML = 'Sending...';
                submitButton.disabled = true;
                
                // Reset after form submission (this would be handled by Django)
                setTimeout(function() {
                    submitButton.innerHTML = originalText;
                    submitButton.disabled = false;
                }, 2000);
            });
        }
    }

    // Search functionality enhancement
    function initSearchEnhancements() {
        const searchInput = document.querySelector('.search-input');
        
        if (searchInput) {
            let searchTimeout;
            
            searchInput.addEventListener('input', function() {
                clearTimeout(searchTimeout);
                
                // Add visual feedback for search
                this.style.borderColor = '#004E89';
                
                // Reset border color after delay
                searchTimeout = setTimeout(() => {
                    this.style.borderColor = '#EAEAEA';
                }, 1000);
            });

            // Clear search on Escape key
            searchInput.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    this.value = '';
                    this.blur();
                }
            });
        }
    }

    // Add animation to elements when they come into view
    function initScrollAnimations() {
        const animatedElements = document.querySelectorAll('.project-card, .blog-item, .skill-category');
        
        if ('IntersectionObserver' in window) {
            const animationObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        animationObserver.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            animatedElements.forEach(function(element) {
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px)';
                element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                animationObserver.observe(element);
            });
        }
    }

    // Copy to clipboard functionality (for code blocks)
    function initCodeCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre code');
        
        codeBlocks.forEach(function(codeBlock) {
            const pre = codeBlock.parentElement;
            const button = document.createElement('button');
            
            button.className = 'copy-code-btn';
            button.innerHTML = 'Copy';
            button.style.cssText = `
                position: absolute;
                top: 10px;
                right: 10px;
                background: #004E89;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
                font-size: 12px;
                cursor: pointer;
                opacity: 0;
                transition: opacity 0.2s ease;
            `;
            
            pre.style.position = 'relative';
            pre.appendChild(button);
            
            pre.addEventListener('mouseenter', function() {
                button.style.opacity = '1';
            });
            
            pre.addEventListener('mouseleave', function() {
                button.style.opacity = '0';
            });
            
            button.addEventListener('click', function() {
                const text = codeBlock.textContent;
                
                if (navigator.clipboard) {
                    navigator.clipboard.writeText(text).then(function() {
                        button.innerHTML = 'Copied!';
                        setTimeout(function() {
                            button.innerHTML = 'Copy';
                        }, 2000);
                    });
                } else {
                    // Fallback for older browsers
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                    
                    button.innerHTML = 'Copied!';
                    setTimeout(function() {
                        button.innerHTML = 'Copy';
                    }, 2000);
                }
            });
        });
    }

    // Initialize all functions when DOM is loaded
    function init() {
        initMobileNav();
        initSmoothScrolling();
        initNavbarScroll();
        initLazyLoading();
        initFormHandling();
        initSearchEnhancements();
        initScrollAnimations();
        initCodeCopyButtons();
        
        // Add loaded class to body for CSS animations
        document.body.classList.add('loaded');
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Handle window resize
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            // Close mobile menu on resize to desktop
            if (window.innerWidth > 768) {
                const navMenu = document.getElementById('nav-menu');
                const navToggle = document.getElementById('nav-toggle');
                
                if (navMenu && navToggle) {
                    navMenu.classList.remove('active');
                    const bars = navToggle.querySelectorAll('.bar');
                    bars.forEach(bar => bar.classList.remove('active'));
                }
            }
        }, 250);
    });

    // Service worker registration (for PWA capabilities)
    if ('serviceWorker' in navigator && window.location.protocol === 'https:') {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js')
                .then(function(registration) {
                    console.log('SW registered: ', registration);
                })
                .catch(function(registrationError) {
                    console.log('SW registration failed: ', registrationError);
                });
        });
    }

})();

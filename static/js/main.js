// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    // Form submission
    const contactForm = document.querySelector('form');
    if (contactForm && contactForm.action.includes('contact')) {
        contactForm.addEventListener('submit', function(e) {
            // Form will submit normally, just show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.textContent = 'Đang gửi...';
                submitBtn.disabled = true;
            }
        });
    }
});

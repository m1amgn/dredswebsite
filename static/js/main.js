function Slider(container) {
  const next = container.querySelector('.slider-next');
  const prev = container.querySelector('.slider-prev');
  next.addEventListener('click', event => moveSlide(true));
  prev.addEventListener('click', event => moveSlide(false));

  function moveSlide(isForward) {
    const currentSlide = container.querySelector('.active');
    const activatedSlide = isForward ? currentSlide.nextElementSibling : currentSlide.previousElementSibling;
    currentSlide.classList.remove('active');
    activatedSlide.classList.add('active');

	  next.disabled = activatedSlide.nextElementSibling ? false : true;
    prev.disabled = activatedSlide.previousElementSibling ? false : true;
  }
}
const sliders = document.querySelectorAll('.slider');
Array.from(sliders).forEach(item => Slider(item));

$(document).ready(function () {
	$('a[href^="#"]').click(function () {
		var target = $(this).attr('href');
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 500);
		return false;
	});
});

$(document).ready(function () {
    var mySwiper = new Swiper ('.image-slider', {
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        spaceBetween: 30,
        slidesPerView: 1.5,
        centeredSlides: true,
        initialSlide: 1,
        loop: true,
        breakpoints: {
            550: {
                    slidesPerView: 2,
               },

            750: {
                slidesPerView: 1.3,
           },

            550: {
                slidesPerView: 2,
           },

            850: {
                slidesPerView: 1.5,
           },

           1200: {
                slidesPerView: 2,
           }
      }
   })
});
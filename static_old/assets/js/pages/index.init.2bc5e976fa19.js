var swiper = new Swiper(".testimonialSlider", {
    loop: !0,
    pagination: { el: ".swiper-pagination", clickable: !0 },
    breakpoints: {
      200: { slidesPerView: 4, spaceBetween: 30 },
      992: { slidesPerView: 4, spaceBetween: 30 },
    },
  }),
  swiper = new Swiper(".homeslider", {
    slidesPerView: "auto",
    loop: !0,
    spaceBetween: 20,
  });

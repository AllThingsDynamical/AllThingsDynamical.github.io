(function () {
  const externalLinks = document.querySelectorAll('a[href^="http"]');
  externalLinks.forEach(link => {
    if (!link.href.includes(window.location.hostname)) {
      link.setAttribute("rel", "noopener noreferrer");
    }
  });
})();
const reloadPage = (() => {
    setTimeout("window.open(self.location, '_self');", 300000);
})();
var nav = document.getElementById('menu-items');

    function toggleNav () {       

        if ( nav.style.display === "" )
        nav.style.display = "block";

        else
        nav.style.display = "";
    }


    function windowResizeHandler () {
        if ( screen.width > 360 )
        nav.style.display = "";
    }

    window.addEventListener("resize", windowResizeHandler);
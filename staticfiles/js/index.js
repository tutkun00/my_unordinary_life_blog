function changeTheme(dark_c, mid_c, accent_c, light_c, font) {
    const root = document.documentElement;

    root.style.setProperty('--color-dark', dark_c);
    root.style.setProperty('--color-mid', mid_c);
    root.style.setProperty('--color-accent', accent_c);
    root.style.setProperty('--color-light', light_c);
    root.style.setProperty('--font-family', font);

    const theme = {dark_c, mid_c, accent_c, light_c, font};
    localStorage.setItem("customTheme", JSON.stringify(theme));
}


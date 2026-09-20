<script>
    import { page } from "$app/stores";

    // Svelte 5 runes for props
    let {
        title,
        description,
        image = "/shipleys-logo.png",
        type = "website",
        jsonLd = null
    } = $props();

    // Compute canonical URL dynamically using $page.url
    const canonicalUrl = $derived($page.url.href);

    // Format title suffix consistently
    const fullTitle = $derived(
        title === "Shipley's Choice Community Association"
            ? title
            : `${title} | Shipley's Choice Community Association`
    );

    // Compute absolute image URL to ensure compatibility across sharing platforms
    const absoluteImage = $derived(
        image.startsWith("http") ? image : `${$page.url.origin}${image}`
    );
</script>

<svelte:head>
    <!-- Primary Meta Tags -->
    <title>{fullTitle}</title>
    <meta name="title" content={fullTitle} />
    <meta name="description" content={description} />
    <link rel="canonical" href={canonicalUrl} />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content={type} />
    <meta property="og:url" content={canonicalUrl} />
    <meta property="og:title" content={fullTitle} />
    <meta property="og:description" content={description} />
    <meta property="og:image" content={absoluteImage} />
    <meta property="og:site_name" content="Shipley's Choice Community Association" />

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content={canonicalUrl} />
    <meta property="twitter:title" content={fullTitle} />
    <meta property="twitter:description" content={description} />
    <meta property="twitter:image" content={absoluteImage} />

    <!-- Search Engine Robots -->
    <meta name="robots" content="index, follow" />

    <!-- Structured Data (JSON-LD) -->
    {#if jsonLd}
        {@html `<script type="application/ld+json">${JSON.stringify(jsonLd)}<\/script>`}
    {/if}
</svelte:head>

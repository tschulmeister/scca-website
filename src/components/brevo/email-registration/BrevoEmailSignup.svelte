<script>
    import { onMount } from "svelte";
    import brevoHtml from "./brevoEmailSignup.htm?raw";

    // Remove any script tags from the html content to avoid rendering static scripts in the body
    const cleanedHtml = brevoHtml.replace(/<script[\s\S]*?<\/script>/gi, "");

    onMount(() => {
        // Set the global variables that the Brevo main.js script expects
        window.REQUIRED_CODE_ERROR_MESSAGE = "Please choose a country code";
        window.LOCALE = "en";
        window.EMAIL_INVALID_MESSAGE = window.SMS_INVALID_MESSAGE =
            "The information provided is invalid. Please review the field format and try again.";
        window.REQUIRED_ERROR_MESSAGE = "This field cannot be left blank. ";
        window.GENERIC_INVALID_MESSAGE =
            "The information provided is invalid. Please review the field format and try again.";
        window.INVALID_NUMBER =
            "The information provided is invalid. Please review the field format and try again.";
        window.INVALID_DATE = "Please enter a valid date";
        window.REQUIRED_MULTISELECT_MESSAGE = "Please select at least 1 option";
        window.translation = {
            common: {
                selectedList: "{quantity} list selected",
                selectedLists: "{quantity} lists selected",
                selectedOption: "{quantity} selected",
                selectedOptions: "{quantity} selected",
            },
        };
        window.AUTOHIDE = false;

        // Load Brevo javascript form handler
        const script = document.createElement("script");
        script.src = "https://sibforms.com/forms/end-form/build/main.js";
        script.defer = true;
        document.body.appendChild(script);

        return () => {
            // Remove any Brevo country dropdowns appended to document.body
            document.querySelectorAll(".sib-sms-select__list").forEach((el) => el.remove());

            // Clean up the script and window variables
            if (document.body.contains(script)) {
                document.body.removeChild(script);
            }
            delete window.REQUIRED_CODE_ERROR_MESSAGE;
            delete window.LOCALE;
            delete window.EMAIL_INVALID_MESSAGE;
            delete window.SMS_INVALID_MESSAGE;
            delete window.REQUIRED_ERROR_MESSAGE;
            delete window.GENERIC_INVALID_MESSAGE;
            delete window.INVALID_NUMBER;
            delete window.INVALID_DATE;
            delete window.REQUIRED_MULTISELECT_MESSAGE;
            delete window.translation;
            delete window.AUTOHIDE;
        };
    });
</script>

<svelte:head>
    <link
        rel="stylesheet"
        href="https://sibforms.com/forms/end-form/build/sib-styles.css"
    />
</svelte:head>

<div class="brevo-signup-wrapper text-left">
    {@html cleanedHtml}
</div>

<style>
    /* Custom CSS to blend Brevo form styles with the site aesthetics */
    :global(.sib-form) {
        background-color: transparent !important;
        padding: 0 !important;
    }
    :global(#sib-container) {
        border: none !important;
        background-color: transparent !important;
        max-width: 100% !important;
        padding: 0 !important;
    }
    :global(#sib-form-container) {
        padding: 0 !important;
    }
    /* Hide default form header/description to prevent redundancy with our page header */
    :global(#sib-container > form > div:nth-child(1)),
    :global(#sib-container > form > div:nth-child(2)) {
        display: none !important;
    }

    /* Fix input, select, and textarea styling to prevent dark mode/browser defaults (e.g., black background or text conflicts) */
    :global(#sib-container .input),
    :global(#sib-container select),
    :global(#sib-container input[type="text"]),
    :global(#sib-container input[type="tel"]),
    :global(#sib-container textarea) {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    :global(#sib-container select option) {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
</style>

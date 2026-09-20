<script>
    import Seo from "$components/Seo.svelte";
    import Mail from "@lucide/svelte/icons/mail";
    import BrevoEmailSignup from "$components/brevo/email-registration/BrevoEmailSignup.svelte";
</script>

<Seo
    title="Register as Resident"
    description="SCCA resident registration form for new and existing homeowners in Sections 1 and 2 of Shipley's Choice."
/>

<section class="page-header py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
            Newsletter Sign-Up
        </p>
        <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
            Register for SCCA Updates
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            Join the official SCCA mailing list powered by Brevo to receive
            newsletters, board notices, and critical community safety
            updates.
        </p>
    </div>
</section>

<section class="max-w-3xl mx-auto px-4 py-12">
    <div
        class="rounded-3xl border border-slate-200 bg-white p-8 sm:p-12 shadow-sm text-center space-y-6"
    >
        <div
            class="mx-auto w-16 h-16 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center border border-blue-100"
        >
            <Mail class="w-8 h-8" />
        </div>

        <div class="space-y-2">
            <h2 class="text-2xl font-bold text-slate-900">
                Official Subscription Form
            </h2>
            <p class="text-slate-600 max-w-lg mx-auto leading-relaxed">
                To complete your registration securely, verify your email, and
                pass security validation, please fill out the official
                subscription form below.
            </p>
        </div>

        <div class="pt-4 flex justify-center">
            <BrevoEmailSignup />
        </div>

        <div class="border-t border-slate-100 pt-6">
            <p class="text-xs text-slate-400 max-w-md mx-auto leading-relaxed">
                Submitting the form adds your email address to the official
                mailing list for Shipley's Choice Community Association (SCCA).
                Your contact information is kept confidential and is never sold
                or shared with external parties.
            </p>
        </div>
    </div>
</section>

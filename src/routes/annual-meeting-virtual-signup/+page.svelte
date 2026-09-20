<script>
    import Seo from "$components/Seo.svelte";
    import Video from "@lucide/svelte/icons/video";
    import Gavel from "@lucide/svelte/icons/gavel";
    import AnnualMeetingVirtualSignup from "$components/brevo/virtual-meeting-signup/2026-annual-meeting/AnnualMeetingVirtualSignup.svelte";
</script>

<Seo
    title="2026 SCCA Annual Membership Meeting Virtual Signup"
    description="Register to receive a private virtual attendance link (Google Meet) for the 2026 SCCA Annual Membership Meeting."
/>

<section class="page-header py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
            October 20, 2026 — Annual Meeting
        </p>
        <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
            2026 SCCA Annual Membership Meeting Virtual Signup
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            If you cannot attend the SCCA Annual Membership Meeting in person on
            October 20, 2026, you can sign up below to receive a private virtual
            link via Google Meet.
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
            <Video class="w-8 h-8" />
        </div>

        <div class="space-y-2">
            <h2 class="text-2xl font-bold text-slate-900">
                Request Virtual Meeting Access
            </h2>
            <p class="text-slate-600 max-w-lg mx-auto leading-relaxed">
                Please complete the secure verification form below. SCCA will
                verify your registration and send the private meeting
                credentials to your email prior to the meeting.
            </p>
        </div>

        <div class="pt-4 flex justify-center">
            <AnnualMeetingVirtualSignup />
        </div>

        <div class="border-t border-slate-100 pt-6">
            <p class="text-xs text-slate-400 max-w-md mx-auto leading-relaxed">
                This registration form is powered by Brevo. The meeting link
                provided is private and intended exclusively for residents of
                Shipley's Choice (Sections 1 & 2). SCCA maintains strict
                confidentiality of resident information.
            </p>
        </div>
    </div>
</section>

<section class="max-w-3xl mx-auto px-4 pb-20">
    <div
        class="rounded-3xl border border-slate-200 bg-white p-8 sm:p-12 shadow-sm space-y-8"
    >
        <div class="flex items-center gap-3 border-b border-slate-100 pb-4">
            <Gavel class="w-6 h-6 text-blue-600" />
            <h2 class="text-2xl font-bold text-slate-900">
                Voting & Attendance Rules
            </h2>
        </div>

        <p class="text-slate-600 leading-relaxed text-sm">
            Please review the official SCCA guidelines established for virtual
            participants joining via Google Meet:
        </p>

        <div class="grid gap-6 sm:grid-cols-2">
            <div class="space-y-2 text-left">
                <h3
                    class="text-base font-bold text-slate-800 flex items-center gap-2"
                >
                    <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                    Absentee Ballots for Votes
                </h3>
                <p class="text-sm text-slate-600 leading-relaxed">
                    <strong
                        >Binding Votes via Official Absentee Ballots Only:</strong
                    >
                    Because verifying identity and household eligibility in
                    real-time for virtual attendees is difficult, binding votes
                    cannot be cast verbally or via chat inside the Google Meet
                    session. Virtual attendees who wish to vote
                    <strong
                        >must submit an official paper absentee ballot</strong
                    > prior to the meeting cutoff.
                </p>
            </div>

            <div class="space-y-2 text-left">
                <h3
                    class="text-base font-bold text-slate-800 flex items-center gap-2"
                >
                    <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                    Quorum Contribution
                </h3>
                <p class="text-sm text-slate-600 leading-relaxed">
                    <strong>Absentee Ballots Count Toward Quorum:</strong> Submitted
                    absentee ballots legally count toward meeting the required 25%
                    household quorum, whether the resident attends virtually or not.
                </p>
            </div>

            <div class="space-y-2 text-left">
                <h3
                    class="text-base font-bold text-slate-800 flex items-center gap-2"
                >
                    <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                    View-Only Format
                </h3>
                <p class="text-sm text-slate-600 leading-relaxed">
                    <strong
                        >Virtual Attendance as View-Only / Floor Discussion:</strong
                    > The Google Meet stream allows remote residents to view board
                    presentations, hear financial/committee reports, and observe floor
                    discussions in real time.
                </p>
            </div>

            <div class="space-y-2 text-left">
                <h3
                    class="text-base font-bold text-slate-800 flex items-center gap-2"
                >
                    <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                    Households Limit
                </h3>
                <p class="text-sm text-slate-600 leading-relaxed">
                    <strong>Two Votes Per Household Limit:</strong> Per Article V,
                    Section 4 of the bylaws, each household in good standing is strictly
                    entitled to two (2) total votes, which are validated against the
                    official membership roster when paper or absentee ballots are
                    submitted.
                </p>
            </div>
        </div>
    </div>
</section>

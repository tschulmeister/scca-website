<script>
    const faqs = [
        {
            question: "What financial safeguards are there?",
            answer: "The laws for SCBDs require strong financial accountability. Key protections include: illegal to co-mingle SCCA and SCBD funds; SCBD funds cannot be used for any purpose not explicitly listed in the petition; officers must be bonded; formal financial reports must be submitted to the County multiple times per year; audits by an independent CPA are required at least once every four years; and the SCBD is not permitted to operate at a deficit in any given year.",
        },
        {
            question: "How much is the assessment expected to be?",
            answer: "While the precise amount depends on the approved budget, the board's preliminary estimate is about $75 per year per household, included in your annual property tax bill. If enacted, SCCA voluntary dues would be significantly reduced.",
        },
        {
            question: "Are there any SCCA expenditures not covered by SCBD?",
            answer: "Yes. SCBD funds cannot be used for routine civic association functions like community newsletters, social events, or advocacy/lobbying. These expenses remain the responsibility of the SCCA.",
        },
        {
            question: "Where can I learn more about SCBD laws and codes?",
            answer: "The law concerning Special Community Benefit Districts is found in Article 4, Title 7 of the Anne Arundel County Code, available on the County’s website at www.aacounty.org. The Office of the Budget has also developed administrative guidelines for establishing and operating these districts.",
        },
        {
            question:
                "Will the SCBD budget be made available to property owners?",
            answer: "Yes. Unlike the SCCA, which operates on a calendar-year cycle, the SCBD operates on the County's fiscal year cycle (July 1 to June 30). Under Article 4, Title 7 of the Anne Arundel County Code, the SCCA (as the administering entity) must prepare the SCBD’s proposed annual budget and submit it to all property owners for their comments by December 31 of each year. The final budget request must be submitted to the County on or before January 31. This separate timeline ensures all owners have ample opportunity to comment on the SCBD budget before it goes to the County for inclusion in their spring budget process.",
        },
        {
            question: "When will the vote take place?",
            answer: "There is no set 'voting day.' Because establishing an SCBD requires the verified signatures of owners representing a two-thirds (2/3) supermajority of all properties, signatures are collected continuously until the threshold is met. Please note that under County guidelines, the official petition and ballot package must be distributed as a standalone mailing and cannot be combined with the regular SCCA annual newsletter. Please look out for this separate, official packet in your mail.",
        },
        {
            question: "How will the assessment be applied?",
            answer: "The assessment will be included as a separate line item on your annual property tax bill as a uniform assessment per tax account.",
        },
        {
            question: "Who is responsible for the SCBD?",
            answer: "The SCCA will be designated as the 'administering entity' under the code. Accordingly, the SCCA Board is responsible for working within Anne Arundel County’s guidelines on all expenditures. Each year, the Board and SCBD Committee create a proposed budget and tax rate, which is submitted to residents for comment by December 31 before being finalized and sent to the County.",
        },
        {
            question: "Where do I mail my signed petition?",
            answer: "Please mail signed petitions to: Shipley’s Choice Community Association, 315 Arbor Oaks Ct, Millersville, MD 21108. In addition to snail mail, residents can send a message to shipleyschoice.scca@gmail.com and a member of the Board will collect your petition in persion. They can also bring it to the October 20 meeting. All received petitions will be forwarded to the Anne Arundel County Budget Office for verification.",
        },
        {
            question: "Who tallies and verifies the petitions?",
            answer: "The County’s SCBD Coordinator reviews and verifies the legitimacy of all signed petitions.",
        },
        {
            question:
                "How are petitions counted, and who must sign the petition?",
            answer: "Each property gets one vote. Both owners (e.g., husband and wife) or all partners in a partnership must sign for the vote to count. Legal entities only require one signature from a representative. If the property is held in a trust, please submit a copy of the first and signature pages of the trust. If an owner is deceased, please provide a copy of the death certificate.",
        },
        {
            question: "What types of uses can the funds be used for?",
            answer: "Funds are strictly limited to the purposes listed in the petition: 1) Maintaining and improving community-owned real and personal property, including open space, recreation property, and entry signs; and 2) Paying administrative expenses (insurance, legal fees, utilities). They CANNOT be used for purposes not listed on the petition.",
        },
        {
            question:
                "Is SCCA subject to the Maryland Homeowners Association Act of 1987?",
            answer: "No, SCCA was formed long before the Act and is not subject to its terms.",
        },
    ];
</script>

<svelte:head>
    <title>SCBD: Some Frequently Asked Questions | SCCA</title>
</svelte:head>

<section class="page-header py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <h1 class="text-4xl font-extrabold tracking-tight">
            SCBD: Some Frequently Asked Questions
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            Answers to common questions regarding the Special Community Benefits
            District proposal. <strong>Please note:</strong> A full standalone packet
            containing comprehensive details and official petition forms will be
            distributed separately to all households—by law, this cannot be combined
            with the regular SCCA annual newsletter.
        </p>
    </div>
</section>

<div class="container mx-auto px-4 py-16">
    <div class="max-w-3xl mx-auto space-y-8">
        {#each faqs as faq}
            <div
                class="bg-white p-6 rounded-xl shadow-sm border border-slate-200"
            >
                <h3 class="text-lg font-bold text-slate-900">{faq.question}</h3>
                <p class="mt-3 text-slate-600 leading-relaxed">{faq.answer}</p>
            </div>
        {/each}

        <div
            class="mt-8 text-center bg-blue-50 p-6 rounded-xl border border-blue-100"
        >
            <p class="text-slate-700">
                Still have questions? The full legal framework can be found in
                Article 4, Title 7 of the Anne Arundel County Code on the <a
                    href="https://www.aacounty.org/"
                    class="app-link">County’s website</a
                >.
            </p>
        </div>
    </div>
</div>

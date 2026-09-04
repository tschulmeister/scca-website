<script>
  // Svelte 5 state rune for tracking active tab
  let activeTab = $state('mission');

  import TrendingUp from "@lucide/svelte/icons/trending-up";
  import ShieldAlert from "@lucide/svelte/icons/shield-alert";
  import Gavel from "@lucide/svelte/icons/gavel";
  import Users from "@lucide/svelte/icons/users";
  import Briefcase from "@lucide/svelte/icons/briefcase";
  import UserCheck from "@lucide/svelte/icons/user-check";
  import FileText from "@lucide/svelte/icons/file-text";
  import Wallet from "@lucide/svelte/icons/wallet";
  import Calendar from "@lucide/svelte/icons/calendar";
  import CheckCircle from "@lucide/svelte/icons/check-circle";
  import Clock from "@lucide/svelte/icons/clock";
  import Play from "@lucide/svelte/icons/play";
  import Sparkles from "@lucide/svelte/icons/sparkles";
  import Flower from "@lucide/svelte/icons/flower";
  import Shield from "@lucide/svelte/icons/shield";
  import BookOpen from "@lucide/svelte/icons/book-open";
</script>

<svelte:head>
  <title>Board | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Governance</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">Shipley's Choice Community Board</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Learn about the Board’s objectives, leadership structure, meeting requirements, 
      and how to connect with the SCCA leadership team.
    </p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12 space-y-12">
  <!-- Tabs Navigation -->
  <div class="flex flex-wrap gap-2 border-b border-slate-200 pb-2">
    <button 
      onclick={() => activeTab = 'mission'}
      class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'mission' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
    >
      Mission & Officers
    </button>
    <button 
      onclick={() => activeTab = 'meetings'}
      class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'meetings' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
    >
      Meetings & Elections
    </button>
    <button 
      onclick={() => activeTab = 'committees'}
      class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'committees' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
    >
      Committees
    </button>
    <button 
      onclick={() => activeTab = 'fullbylaws'}
      class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'fullbylaws' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
    >
      Full By-Laws
    </button>
  </div>

  <!-- Tab Content -->
  <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm min-h-[400px]">
    {#if activeTab === 'mission'}
      <div class="space-y-8">
        <!-- Header Info -->
        <div class="border-b pb-4">
          <h2 class="text-2xl font-extrabold text-slate-900">Objectives & SCCA Mission (Articles I & II)</h2>
          <p class="text-slate-500 text-sm mt-1">
            Incorporated July 8, 1980, the Shipley's Choice Community Association operates under Maryland law to protect community aesthetics and enhance neighborhood welfare.
          </p>
        </div>

        <!-- SCCA Core Objectives -->
        <div class="grid gap-6 sm:grid-cols-3">
          <div class="p-5 rounded-2xl bg-blue-50/40 border border-blue-100 flex flex-col justify-between space-y-3">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <div class="p-2 bg-blue-100 text-blue-800 rounded-xl flex-shrink-0">
                  <TrendingUp class="w-5 h-5" />
                </div>
                <h4 class="font-bold text-slate-900 leading-tight">1. Promote Welfare & Value</h4>
              </div>
              <p class="text-slate-600 text-xs md:text-sm leading-relaxed pl-1">
                Encouraging cooperative resident projects designed to improve general welfare and protect property appearance, convenience, and home values.
              </p>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-blue-50/40 border border-blue-100 flex flex-col justify-between space-y-3">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <div class="p-2 bg-blue-100 text-blue-800 rounded-xl flex-shrink-0">
                  <ShieldAlert class="w-5 h-5" />
                </div>
                <h4 class="font-bold text-slate-900 leading-tight">2. Discourage Violations</h4>
              </div>
              <p class="text-slate-600 text-xs md:text-sm leading-relaxed pl-1">
                Enforcing compliance with land restrictions, covenants, and plat filing rules established across Shipley's Choice Sections 1 through 5.
              </p>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-blue-50/40 border border-blue-100 flex flex-col justify-between space-y-3">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <div class="p-2 bg-blue-100 text-blue-800 rounded-xl flex-shrink-0">
                  <Gavel class="w-5 h-5" />
                </div>
                <h4 class="font-bold text-slate-900 leading-tight">3. Execute Charter Powers</h4>
              </div>
              <p class="text-slate-600 text-xs md:text-sm leading-relaxed pl-1">
                Exercising all necessary corporate legal authorities and executive directives as designated in the Charter of the Corporation.
              </p>
            </div>
          </div>
        </div>

        <!-- Executive Stewardship Overview Box -->
        <div class="rounded-3xl border border-slate-200 bg-slate-50/50 p-6 md:p-8 space-y-4">
          <div class="flex items-center gap-3">
            <Users class="w-6 h-6 text-slate-700" />
            <h3 class="text-lg font-bold text-slate-900">Executive Stewardship & Board Composition (Article VIII)</h3>
          </div>
          <p class="text-slate-700 text-sm leading-relaxed">
            The executive governance is vested in a Board of Directors, all of whom must remain members in good standing. 
            The Board consists of four core officers (President, Vice President, Secretary, Treasurer) and a minimum of four (4) elected Directors. 
            To accommodate community expansion, the Board has discretion to scale up to a maximum of fifteen (15) elected Directors. 
            A quorum of five (5) Directors is strictly required for the conduct of any business at quarterly Board sessions.
          </p>
        </div>

        <!-- Officers Duties Section -->
        <div class="space-y-4">
          <h3 class="text-xl font-bold text-slate-900 border-b pb-2">Core SCCA Officers & Specific Duties</h3>
          <div class="grid gap-6 md:grid-cols-2">
            <!-- President Card -->
            <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-3 hover:border-slate-300 transition-all duration-200">
              <div class="space-y-2">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-blue-100 text-blue-800 rounded-xl">
                    <Briefcase class="w-5 h-5" />
                  </div>
                  <h4 class="font-bold text-slate-900">President</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                  Presides over all official meetings of the Association and the Board of Directors. Operates as an ex-officio member of all Standing and Special Committees. Forwards progress reports of Association activities to all members.
                </p>
              </div>
            </article>

            <!-- Vice President Card -->
            <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-3 hover:border-slate-300 transition-all duration-200">
              <div class="space-y-2">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-emerald-100 text-emerald-800 rounded-xl">
                    <UserCheck class="w-5 h-5" />
                  </div>
                  <h4 class="font-bold text-slate-900">Vice President</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                  Assumes all presidential powers, duties, and executive responsibilities when the President is absent or when such duties are officially assigned. Serves permanently as the Chairman of the Membership Committee.
                </p>
              </div>
            </article>

            <!-- Secretary Card -->
            <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-3 hover:border-slate-300 transition-all duration-200">
              <div class="space-y-2">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-amber-100 text-amber-800 rounded-xl">
                    <FileText class="w-5 h-5" />
                  </div>
                  <h4 class="font-bold text-slate-900">Secretary</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                  Records and preserves precise minutes of all general and Board sessions. Presents interim progress summaries to members. Manages and signs SCCA correspondence to external organizations. Holds custody of all archives.
                </p>
              </div>
            </article>

            <!-- Treasurer Card -->
            <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-3 hover:border-slate-300 transition-all duration-200">
              <div class="space-y-2">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-purple-100 text-purple-800 rounded-xl">
                    <Wallet class="w-5 h-5" />
                  </div>
                  <h4 class="font-bold text-slate-900">Treasurer</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                  Has care, custody, and full responsibility for SCCA's financial accounts. Secured by corporate bond. Issues all disbursements, with checks requiring a co-signature. Submits records to an annual October Auditing Committee.
                </p>
              </div>
            </article>
          </div>
        </div>
      </div>
    {:else if activeTab === 'meetings'}
      <div class="space-y-8">
        <!-- Header Info -->
        <div class="border-b pb-4">
          <h2 class="text-2xl font-extrabold text-slate-900">Meetings & Democratic Voting (Articles V & VI)</h2>
          <p class="text-slate-500 text-sm mt-1">
            SCCA is governed through quarterly resident forums, strict quorum mandates, two-year office limits, and secure absentee voting.
          </p>
        </div>

        <div class="grid gap-6 md:grid-cols-2">
          <!-- Meetings & Special Sessions -->
          <div class="space-y-4 p-6 rounded-2xl bg-slate-50 border border-slate-200">
            <h3 class="font-bold text-slate-900 flex items-center gap-2">
              <Calendar class="w-5 h-5 text-blue-600" />
              Association Schedule & Notices
            </h3>
            <ul class="space-y-3 text-slate-700 text-sm leading-relaxed">
              <li>
                <strong>Four Regular Meetings:</strong> Held annually. The crucial budget-adopting session occurs in January, while the Annual Meeting and general elections are held in October. Spring and summer sessions are held in April and July.
              </li>
              <li>
                <strong>Special Sessions:</strong> Can be triggered immediately by the President, a majority Board vote, or a signed written petition by at least 25% of active community members.
              </li>
              <li>
                <strong>Notice Regulations:</strong> Seven (7) days written notice is legally required for all regular sessions. A fourteen (14) day written notice is mandatory for any meeting involving Bylaw modifications.
              </li>
            </ul>
          </div>

          <!-- Quorum & Voting Privileges -->
          <div class="space-y-4 p-6 rounded-2xl bg-slate-50 border border-slate-200">
            <h3 class="font-bold text-slate-900 flex items-center gap-2">
              <CheckCircle class="w-5 h-5 text-emerald-600" />
              Quorum & Voting Control
            </h3>
            <ul class="space-y-3 text-slate-700 text-sm leading-relaxed">
              <li>
                <strong>Quorum Requirements:</strong> Twenty-five percent (25%) of voting members constitutes a quorum. Confirmed absentee ballots count toward establishing the presence of a quorum for the Annual Meeting.
              </li>
              <li>
                <strong>Household Limits:</strong> Restricted to exactly two (2) voting privileges per household, exercised by qualified adult members. Special (non-resident) members hold no voting rights and cannot hold office.
              </li>
              <li>
                <strong>Majorities:</strong> Regular items pass by a simple majority vote. However, By-Law amendments and annual assessments exceeding $5.00 require a strict two-thirds (2/3) supermajority.
              </li>
            </ul>
          </div>
        </div>

        <!-- Elections & Dues Timeline Dashboard -->
        <div class="rounded-3xl border border-slate-200 bg-slate-50/50 p-6 md:p-8 space-y-6">
          <h3 class="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Clock class="w-5 h-5 text-slate-700" />
            SCCA Annual Election & Fiscal Timeline
          </h3>

          <div class="grid gap-6 md:grid-cols-4 text-xs md:text-sm text-slate-700 leading-relaxed">
            <!-- Timeline Item 1 -->
            <div class="p-4 bg-white border border-slate-100 rounded-xl space-y-1.5 shadow-sm">
              <span class="px-2 py-0.5 bg-blue-100 text-blue-800 text-2xs font-extrabold rounded-md uppercase">July</span>
              <p class="font-bold text-slate-950">Appoint Nominators</p>
              <p class="text-xs text-slate-600">The President appoints a representative Nominating Committee tasked with researching and selecting candidates for open seats.</p>
            </div>

            <!-- Timeline Item 2 -->
            <div class="p-4 bg-white border border-slate-100 rounded-xl space-y-1.5 shadow-sm">
              <span class="px-2 py-0.5 bg-blue-100 text-blue-800 text-2xs font-extrabold rounded-md uppercase">Late September</span>
              <p class="font-bold text-slate-950">Ballot Distribution</p>
              <p class="text-xs text-slate-600">Exactly two weeks prior to the Annual Meeting, the Secretary mails candidate names and official absentee ballots to all households.</p>
            </div>

            <!-- Timeline Item 3 -->
            <div class="p-4 bg-white border border-slate-100 rounded-xl space-y-1.5 shadow-sm">
              <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 text-2xs font-extrabold rounded-md uppercase">October 1st</span>
              <p class="font-bold text-slate-950">Fiscal Dues Open</p>
              <p class="text-xs text-slate-600">Annual dues become due and payable. In addition, the general elections are executed via secret written ballots at the October Annual Meeting.</p>
            </div>

            <!-- Timeline Item 4 -->
            <div class="p-4 bg-white border border-slate-100 rounded-xl space-y-1.5 shadow-sm">
              <span class="px-2 py-0.5 bg-red-100 text-red-800 text-2xs font-extrabold rounded-md uppercase">January 1st</span>
              <p class="font-bold text-slate-950">Dues Arrears Deadline</p>
              <p class="text-xs text-slate-600">Dues are officially in arrears. Failure to pay terminates good standing, privileges, and facility access under Article VII.</p>
            </div>
          </div>
        </div>
      </div>
    {:else if activeTab === 'committees'}
      <div class="space-y-8">
        <div class="border-b pb-4">
          <h2 class="text-2xl font-extrabold text-slate-900">Standing Committees (Article IX)</h2>
          <p class="text-slate-500 text-sm mt-1">
            The SCCA Board appoints Chairmen to five Standing Committees to oversee day-to-day community operations. Each committee consists of no less than three members, including one designated Board member.
          </p>
        </div>

        <!-- 5 Committees Grid -->
        <div class="grid gap-6 md:grid-cols-2">
          <!-- Membership Card -->
          <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-4">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <Users class="w-5 h-5 text-blue-600" />
                  Membership Committee
                </h3>
                <span class="px-2.5 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full">Chaired by Vice President</span>
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Promotes membership within the Association, maintains a current resident and member directory, assists the Treasurer in preparing dues statements, and coordinates community promotion with the Social Committee.
              </p>
              <div class="p-3 bg-white border border-slate-100 rounded-xl">
                <p class="text-xs font-semibold text-slate-900">Sub-committee: Welcome Committee</p>
                <p class="text-xs text-slate-600 mt-1">Calls on new residents within thirty (30) days of moving in to present the By-Laws and welcome them to Shipley's Choice.</p>
              </div>
            </div>
          </article>

          <!-- Recreational Card -->
          <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-4">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <Play class="w-5 h-5 text-emerald-600" />
                  Recreational Committee
                </h3>
                <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-full">Board Appointed</span>
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Plans and executes the development and upkeep of all recreational areas. This committee prepares an annual budget of operating and construction expenditures, establishes Rules of Conduct, and sets appropriate user fees.
              </p>
            </div>
          </article>

          <!-- Social Card -->
          <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-4">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <Sparkles class="w-5 h-5 text-purple-600" />
                  Social Committee
                </h3>
                <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-full">Board Appointed</span>
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Plans, schedules, and administers all official social functions and community celebrations in Shipley's Choice. Prepares an annual operating budget for presentation and approval by the Board of Directors.
              </p>
            </div>
          </article>

          <!-- Beautification Card -->
          <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-4">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <Flower class="w-5 h-5 text-teal-600" />
                  Beautification Committee
                </h3>
                <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-full">Board Appointed</span>
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Promotes aesthetic standards across the neighborhood. Oversees the professional landscaping and maintenance of all entrance properties, schedules community cleanliness campaigns, and encourages residents to maintain high yard care standards.
              </p>
            </div>
          </article>

          <!-- Architectural Card -->
          <article class="p-6 rounded-2xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between space-y-4 md:col-span-2">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <Shield class="w-5 h-5 text-red-600" />
                  Architectural & Safety Committee
                </h3>
                <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-full">Board Appointed</span>
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Promotes resident and facility safety. Corrects identified unsafe activities, raises community awareness around potential neighborhood hazards, and manages architectural compliance reviews. Composed of officers and interested residents.
              </p>
            </div>
          </article>
        </div>

        <!-- General Committee Rules Summary Box -->
        <div class="rounded-3xl border border-slate-200 bg-slate-50/50 p-6 md:p-8 space-y-4">
          <div class="flex items-center gap-2">
            <BookOpen class="w-5 h-5 text-slate-700" />
            <h3 class="text-lg font-bold text-slate-900">
              Bylaw Rules Governing SCCA Committees (Article IX, Section 1, 4)
            </h3>
          </div>
          <div class="grid gap-6 md:grid-cols-3 text-sm text-slate-700 leading-relaxed">
            <div class="space-y-1.5">
              <p class="font-bold text-slate-900">1. Committee Size & Reporting</p>
              <p>Each committee must consist of no less than three (3) members. A designated member of the Board of Directors is appointed by the President to report the committee's activities directly to the Board.</p>
            </div>
            <div class="space-y-1.5">
              <p class="font-bold text-slate-900">2. Budget Approvals</p>
              <p>All committees prepare and submit an operating budget to the Board of Directors by December 15 each year. These are merged into the General Budget submitted to the general membership at the January meeting.</p>
            </div>
            <div class="space-y-1.5">
              <p class="font-bold text-slate-900">3. Spending Limits</p>
              <p>Prior to formal budget approval, Committee Chairmen may commit up to $100.00 in expenditures by securing combined approval from both the SCCA President and Treasurer. All excess amounts require full Board approval.</p>
            </div>
          </div>
        </div>
      </div>
    {:else if activeTab === 'fullbylaws'}
      <div class="space-y-12 text-slate-800">
        <!-- Historical Memoramdum Styled Box -->
        <div class="rounded-3xl border border-amber-200 bg-amber-50/40 p-6 md:p-8 shadow-sm">
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-amber-200/60 pb-4 mb-4 text-xs font-semibold uppercase tracking-wider text-amber-800">
            <span>Historical Memoramdum</span>
            <span>July 29, 1980</span>
          </div>
          <div class="space-y-4 text-slate-700 leading-relaxed text-sm md:text-base">
            <p class="font-bold text-slate-900 text-lg">SHIPLEY'S CHOICE COMMUNITY ASSOCIATION, INCORPORATED</p>
            <p class="text-slate-500 font-medium">Millersville, Maryland</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 border-y border-amber-200/40 py-3 text-xs md:text-sm font-medium">
              <p><span class="text-amber-800 font-bold">TO:</span> All Residents, Shipley's Choice</p>
              <p><span class="text-amber-800 font-bold">FROM:</span> Bill Thompson, President (signed: Bill Thompson)</p>
              <p class="sm:col-span-2"><span class="text-amber-800 font-bold">SUBJECT:</span> Status of Incorporation</p>
            </div>
            <p>
              Please be advised that on July 8, 1980 the Incorporation of the Shipley's Choice Community Association was approved and recorded by the State of Maryland Department of Assessments and Taxation.
            </p>
            <p>
              The enclosed By-Laws, which were approved by the Association, were also approved by the State and a "corrected copy" of the By-Laws as recorded is attached for your information and future reference. Please destroy the earlier copy which was provided prior to approval of the Association.
            </p>
            <p>
              Now that the Association has been formally resolved we will set about to establish a formal Bank Account, as soon as we get our Federal Tax number. You will also be pleased to know that after all was said & done and considerable work done by the Board, the total cost of the Incorporation effort was accomplished for a total of $40.00, which was a far cry from the earlier estimate of several hundred dollars. The Board will continue to "squeeze" every penny of Association money to a maximum benefit of the Association.
            </p>
            <p class="pt-2 font-semibold text-slate-900">
              My personal thanks to all those who helped in this effort.
            </p>
          </div>
        </div>

        <!-- Word-for-Word Bylaws Document -->
        <div class="space-y-12">
          <div class="text-center border-b pb-8">
            <h2 class="text-3xl font-black text-slate-950 tracking-tight uppercase">BY-LAWS</h2>
            <p class="text-sm font-semibold uppercase tracking-[0.24em] text-blue-600 mt-2">OF</p>
            <h3 class="text-xl font-bold text-slate-800 mt-2">THE SHIPLEY'S CHOICE COMMUNITY ASSOCIATION, INC.</h3>
          </div>

          <!-- ARTICLE I -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE I</span>
              <h4 class="text-xl font-extrabold text-slate-900">Name of the Association</h4>
            </div>
            <p class="text-slate-700 leading-relaxed pl-1">
              The name of this association shall be the Shipley's Choice Community Association, Inc.
            </p>
          </section>

          <!-- ARTICLE II -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE II</span>
              <h4 class="text-xl font-extrabold text-slate-900">Objectives of the Association</h4>
            </div>
            <p class="text-slate-600 leading-relaxed pl-1 text-sm font-semibold">
              The objectives of this Association are:
            </p>
            <ol class="space-y-4 pl-1">
              <li class="flex gap-4 items-start p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm">
                <span class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center font-bold text-sm">1</span>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  To encourage the residents in Shipley's Choice cooperatively into such projects as will promote the general welfare, improve and protect the appearance, value and convenience of property in Shipley's Choice.
                </p>
              </li>
              <li class="flex gap-4 items-start p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm">
                <span class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center font-bold text-sm">2</span>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  To promote a compliance with and to discourage violations of any of the real estate situated within the limits of Shipley's Choice Sections 1, 2, 3, 4 and 5, as such restrictions as are designed, set forth, and incorporated in all original deeds executed by Harry E. Gorin and others, in Declarations made by Gorin Brothers, Inc. and others, in Declarations made by Benfield Boulevarde, Inc. and others, and in Declarations made by Monumental Properties, Inc. and others, all recorded or to be recorded in the Deed and Plat Records of Anne Arundel County.
                </p>
              </li>
              <li class="flex gap-4 items-start p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm">
                <span class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center font-bold text-sm">3</span>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  To exercise all the powers and authorities which are set forth and designated in the Charter of this Corporation.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE III -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE III</span>
              <h4 class="text-xl font-extrabold text-slate-900">Membership Classifications</h4>
            </div>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Limit Per Household</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Membership in this Association shall be limited to one (1) membership per household.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Three Types of Membership</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed mb-2">
                  The membership of the Association shall consist of three types, namely:
                </p>
                <ul class="list-disc list-inside pl-4 space-y-1 text-slate-700 text-sm md:text-base font-medium">
                  <li>(a) Members</li>
                  <li>(b) Associate Members</li>
                  <li>(c) Special Members</li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">3. Qualifications for Membership</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed mb-2">
                  The qualifications for membership for each of said three types shall be as follows:
                </p>
                <ul class="pl-4 space-y-3 text-slate-700 text-sm md:text-base">
                  <li class="leading-relaxed">
                    <strong>◦ (a) Members:</strong> Any person who owns and resides on property (as defined in ARTICLE II) or any person or persons in the immediate family of such property owner, residing therein; such as sons, daughters, parents, shall be eligible for privileges of the Association as hereinafter provided.
                  </li>
                  <li class="leading-relaxed">
                    <strong>◦ (b) Associate Members:</strong> Any person living within the area as defined in ARTICLE II as a year around resident, in a house or apartment rented by him, but who does not own property within the limits of the area defined in ARTICLE II, shall be eligible to become an Associate Member, as hereinafter provided.
                  </li>
                  <li class="leading-relaxed">
                    <strong>◦ (c) Special Members:</strong> Any person who owns property as defined in ARTICLE II, but who does not reside thereon, shall be eligible to become a Special Member.
                  </li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">4. Voting Privileges</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  There shall be two voting privileges for each household, which may be exercised by any one or two members of that household who qualify for membership in this Association, except that Special Members shall have no vote or a right to hold office.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">5. Change of Status</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  If, after admission to membership, the status of any member shall change, his membership shall be immediately terminated unless such person can and does, simultaneously with such change of status, qualify for a membership under one of the other classifications established by this Article, in which event he shall continue to be a member of the Association under the classification which properly describes his new status.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">6. Termination of Membership</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed mb-2">
                  Membership in the Association may be terminated:
                </p>
                <ul class="pl-4 space-y-2 text-slate-700 text-sm md:text-base">
                  <li><strong>◦ (a)</strong> Upon the request of the member.</li>
                  <li><strong>◦ (b)</strong> Upon failure to maintain good standing because of non-payment of dues or assessments within the time designated in the By-Laws.</li>
                  <li><strong>◦ (c)</strong> Upon determination by the Board of Directors that any member's children, or any resident in said member's home, has flagrantly or continuously acted contrary to the objectives and purposes of the Association or has violated the By-Laws and Rules of this Association.</li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">7. Reinstatement Procedure</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Application for reinstatement shall be initiated by the member in question and shall be submitted in writing to the Board of Directors. The Board of Directors shall have the authority to act upon said request.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">8. Admissions</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The Board of Directors, upon the recommendation of the Membership Committee, shall confirm the qualifications of new members and after due investigation of such qualifications as referred to in ARTICLE III shall admit such new members into the Association.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE IV -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE IV</span>
              <h4 class="text-xl font-extrabold text-slate-900">Membership Privileges & Responsibilities</h4>
            </div>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Ordinary Use of Facilities</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Membership in good standing shall entitle members and their guests to the ordinary use of all Association facilities, subject to the Rules established by the appropriate committees of this Association.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Accompanied Guests Only</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Any guest using Association facilities must be accompanied by a member. No resident of Shipley's Choice may qualify as a guest.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">3. Use At Own Risk</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  All persons who use Association facilities do so at their own risk.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">4. Exclusivity to Members</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Any facilities erected or purchased and improved by the Shipley's Choice Community Association shall only be enjoyed by members of the Association in good standing, and their guests.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE V -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE V</span>
              <h4 class="text-xl font-extrabold text-slate-900">Meetings of the Association</h4>
            </div>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Four Regular Annual Meetings</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  There shall be at least four regular meetings of the Association in each year; the annual meeting, which shall be held in October of each year on such day as the Board of Directors shall select; and the three remaining meetings shall be held in January, April and July of each year on such day as the Board of Directors or membership shall select.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Special Meetings</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  A special meeting may be called at any time by the President, by a majority vote of the Board of Directors, or must be called upon written signed petition stating reasons therefore by 25% of the members in good standing.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">3. Written Notice Periods</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed font-semibold mb-2">
                  Notice of all meetings of the Association, both regular and special, shall be given to all members of the Association by written notice at least:
                </p>
                <ul class="list-disc list-inside pl-4 space-y-1 text-slate-700 text-sm md:text-base">
                  <li><strong>Seven (7) days</strong> before such date set for the meeting.</li>
                  <li><strong>Fourteen (14) days</strong> before any meeting at which amendments to the By-Laws may be voted on.</li>
                </ul>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed pt-2">
                  This notice in cases of special meetings shall include a general statement of the matters to be discussed, and the issues to be presented to the members for decision. The agenda of special meetings shall be restricted thereto.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">4. Quorum Definition</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Twenty-five percent of the voting members shall constitute a quorum, except as qualified in ARTICLE VI, provided that notification to all members as to time, place and purpose of such meeting shall have been sent as provided in this ARTICLE.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">5. Parliamentary Authority</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  All meetings shall be conducted by the chair in accordance with established Roberts Rules of Parliamentary procedure.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE VI -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE VI</span>
              <h4 class="text-xl font-extrabold text-slate-900">Voting</h4>
            </div>
            <p class="text-slate-700 leading-relaxed pl-1">
              Provided a quorum is present, as defined in ARTICLE V, majority voice of members present at any meeting of the Association shall be sufficient to carry any motion or decide any issue except:
            </p>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Amendments to By-Laws</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Such amendments shall require a two-thirds vote of the voting members present, provided a quorum is present.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Election of Officers and Directors</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Such election shall be held at the October meeting of the Association, at which time Officers and Directors shall be elected for a two-year term to fill the vacancies which occur at that time. At the July meeting the President shall appoint a representative Nominating Committee who shall select nominees for office. No later than two weeks prior to the October meeting the Secretary shall notify the membership of the selections of the Nominating Committee, enclosing absentee ballots to be returned to the Secretary by those who are not able to vote in person. The results of such absentee ballots shall be kept secret until the written votes of those present at the October meeting are counted. Voting shall be by written ballot by those present at the October meeting and all official absentee ballots returned to the Secretary and vacancies shall be filled by the individuals receiving the highest number of votes cast. Absentee ballots shall be considered in determining the presence of a quorum. Nominations for vacancies may also be made from the floor prior to election. The newly elected Officers and Directors shall meet with the retiring Officers and Directors not later than two weeks following the election, at which time they will take office. The retiring President shall preside for the election of officers and shall execute the changes in responsibilities from the retiring officers to the incoming officers.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">3. Assessments Over $5.00</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Membership assessments in excess of five ($5.00) dollars per year shall require the same procedure as amending the By-Laws.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE VII -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE VII</span>
              <h4 class="text-xl font-extrabold text-slate-900">Dues</h4>
            </div>
            <p class="text-slate-700 leading-relaxed pl-1 text-sm md:text-base">
              The amount of dues for membership shall be recommended for each year by the Officers and Board of Directors at the meeting so designated. The recommendation must be voted upon and if the motion is lost, the dues will revert to the amount of the previous year. Dues shall be due and payable October first and shall be deemed to be in arrears on and after January first of the next year.
            </p>
          </section>

          <!-- ARTICLE VIII -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE VIII</span>
              <h4 class="text-xl font-extrabold text-slate-900">Duties of Officers and Directors</h4>
            </div>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Executive Power & Budgeting</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The executive power of the Association shall be vested in the Officers and Directors all of whom must be members in good standing. Upon taking office the Officers and Directors shall prepare an operating budget for the year, submitting this budget for approval by the membership at the January meeting. If any additions, deletions, or revisions are voted on the membership, such changes shall be instituted by the Board of Directors provided the total budget presented is not in excess of funds available as determined by the Board of Directors.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Board Composition Criteria</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed mb-2">
                  The number of members on the Board of Directors shall be established each year by the Board within the limitations of the following criteria:
                </p>
                <ul class="pl-4 space-y-2 text-slate-700 text-sm md:text-base">
                  <li>
                    <strong>◦ (a)</strong> The elected positions of President, Vice President, Secretary and Treasurer shall be members of the Board of Directors.
                  </li>
                  <li>
                    <strong>◦ (b)</strong> In addition there shall be at least four (4) elected Directors, initially with two (2) elected for a one year term and the others elected for a two (2) year term. Thereafter, all Directors to serve a term of two (2) years. The immediate past President shall become a member of the Board.
                  </li>
                  <li>
                    <strong>◦ (c)</strong> As the size of the community increases the Board, may at its discretion, increase the number of elected Directors for the following year to a total not to exceed fifteen (15).
                  </li>
                  <li>
                    <strong>◦ (d)</strong> The determination of the size for the following year shall be done at a Board meeting in advance of the appointment of the Nominating Committee to select candidates for the coming year.
                  </li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">3. Terms of Office</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The President, Vice President, Secretary and Treasurer shall be elected by general membership during the annual meeting in October. Terms of office shall be two (2) years.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">4. Vacancies</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Vacancies which occur in the Board of Directors, including Directors and officers, otherwise than by expiration of term of office, shall be filled by majority vote of the Board and the individual so selected shall serve until the next annual election.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">5. Quarterly Board Meetings</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The Board of Directors shall hold meetings at least quarterly with such rules as they may prescribe. A quorum for the conduct of any business shall consist of five (5) members. The President may, with concurrence of five (5) members of the Board, cancel any quarterly meeting.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">6. Specific Duties of Officers</p>
                <ul class="pl-4 space-y-3 text-slate-700 text-sm md:text-base">
                  <li>
                    <strong>◦ (a) President:</strong> The President shall preside at all meetings of the Association and of the Board of Directors. The President shall be an ex-officio member of all Standing and Special Committees. The President shall forward reports of the activities of the Association to all members.
                  </li>
                  <li>
                    <strong>◦ (b) Vice President:</strong> The Vice President shall have all duties and responsibilities of the President when absent or when such duties are assigned by the President. The Vice President shall be Chairman of the Membership Committee, whose duties are hereinafter defined.
                  </li>
                  <li>
                    <strong>◦ (c) Secretary:</strong> The Secretary shall keep the minutes of all meetings of the Association and of the Board of Directors. At all membership meetings the Secretary shall present a summary report of all action taken by the Board of Directors in the interim period between meetings. The Secretary shall be responsible for written communications with individuals or organizations outside the Association, subject to the approval of the Board of Directors. The Secretary shall be custodian of all correspondence of the Association.
                  </li>
                  <li>
                    <strong>◦ (d) Treasurer:</strong> The Treasurer shall have care and custody of and be responsible for all funds and finances of the Association subject to the direction and supervision of the Board of Directors. The Treasurer shall give bond to be paid for by the Association. The Treasurer shall make all disbursements for the Association by check, all checks being countersigned by one (1) of the following: (1) President, (2) Vice-President, or (3) Secretary.
                  </li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">7. Audits & Reporting</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The Treasurer shall prepare statements for presentation to the Board of Directors and to general meetings. The Treasurer shall submit all records to the Special Auditing Committee appointed by the President at least thirty (30) days prior to the annual meeting in October, this committee presenting an audit to the President before the transfer of responsibility at the Board of Directors meeting following the annual meeting.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE IX -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE IX</span>
              <h4 class="text-xl font-extrabold text-slate-900">Committees</h4>
            </div>
            <ol class="space-y-4 pl-1">
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">1. Standing Committees Definition</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  There shall be such Standing Committees as enumerated below, the Chairman being appointed by the President and announced to the membership at the October meeting. There shall be no less than three (3) members to a Standing Committee. One member of each Standing Committee shall be a member of the Board of Directors, designated by the President, who will report Committee activities to the Board. Members of Standing Committees are to be appointed by the committee Chairman immediately following his appointment. The President shall be an ex-officio member of all Standing Committees and as such shall be notified of all committee meetings.
                </p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed pt-2">
                  Each Standing Committee shall prepare an operating budget, submitting it no later than December 15, to the Board of Directors for their approval and/or revision. The budgets of all committees as approved by the Board of Directors shall be included in the General Budget to be submitted to the membership at the January meeting.
                </p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed pt-2">
                  The Chairman of all Standing Committees shall submit interim reports at all general membership meetings, and at the October meeting, they shall submit a comprehensive written report of activities during the preceding year.
                </p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed font-semibold pt-2">
                  The Standing Committees shall be as follows:
                </p>
                <ul class="list-disc list-inside pl-4 space-y-1 text-slate-700 text-sm md:text-base">
                  <li>(a) Membership</li>
                  <li>(b) Recreational</li>
                  <li>(c) Social</li>
                  <li>(d) Beautification</li>
                  <li>(e) Architectural</li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">2. Standing Committees Duties</p>
                <ul class="pl-4 space-y-3 text-slate-700 text-sm md:text-base">
                  <li>
                    <strong>◦ (a) Membership:</strong> The Vice President of the Association shall be Chairman of the Membership Committee. This committee shall promote membership in the Association; maintain a current directory of members and residents including addresses and telephone numbers; assist the Treasurer in preparing statements of dues; co-ordinate promotional activities with Social Committee; and in general control all activities pertaining to promoting and maintaining a substantial roster of members to residents. A sub-committee, known as the Welcome Committee, shall be established to call on all new residents of Shipley's Choice within thirty (30) days of their establishment of residence, present a copy of the By-Laws and explain the activities of the Association.
                  </li>
                  <li>
                    <strong>◦ (b) Recreational:</strong> This Committee shall plan and execute the development of recreational areas, prepare an annual budget of operating and construction expenditures, establish Rules of Conduct and fees, and in general exercise control of all recreational activities, subject to approval by the Board of Directors.
                  </li>
                  <li>
                    <strong>◦ (c) Social:</strong> This Committee shall plan and administer all social functions and shall prepare an operating budget for presentation to the Board of Directors.
                  </li>
                  <li>
                    <strong>◦ (d) Beautification:</strong> This Committee shall generally promote beautification of Shipley's Choice, maintain all entrance properties, sponsor cleanliness campaigns, and encourage residents to maintain high standards in the landscaping of individual lots. The Committee shall prepare an annual budget of operating expenses.
                  </li>
                  <li>
                    <strong>◦ (e) Architectural:</strong> This Committee shall generally promote the safety in Shipley's Choice by making residents and persons using Shipley's Choice facilities aware of unsafe activities and correcting unsafe activities as deemed necessary. The members of this Committee should include officers and residents interested in safety. The Committee shall prepare reports of its activities as required by the President and shall also prepare an annual budget of operating expenses.
                  </li>
                </ul>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-950 font-bold text-sm md:text-base">3. Special Committees</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  The President shall appoint such other Special Committees as deemed necessary. The President shall be an ex-officio member of all Special Committees and shall be notified of all meetings. The Chairman of all Special Committees shall submit a written report of the Committee's activities upon completion of duties, said final report to be included in the minutes by the Secretary.
                </p>
              </li>
              <li class="p-4 rounded-2xl bg-slate-50 border border-slate-100 shadow-sm space-y-2">
                <p class="text-slate-900 font-bold text-sm md:text-base">4. Committee Spending Authorization</p>
                <p class="text-slate-700 text-sm md:text-base leading-relaxed">
                  Subsequent to their appointment and prior to budget approval by the membership, Committee Chairmen can commit expenditures up to $100.00 by securing approval of the President and Treasurer. Any expenditure in excess of this amount will require the approval of the Board of Directors.
                </p>
              </li>
            </ol>
          </section>

          <!-- ARTICLE X -->
          <section class="space-y-4">
            <div class="flex items-center gap-4">
              <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase">ARTICLE X</span>
              <h4 class="text-xl font-extrabold text-slate-900">Order of Business</h4>
            </div>
            <p class="text-slate-600 leading-relaxed pl-1 text-sm font-semibold">
              At Regular Meetings the Order of Business shall be as follows:
            </p>
            <ol class="grid grid-cols-1 sm:grid-cols-2 gap-3 pl-1 text-sm text-slate-800 font-medium">
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">1</span> Reading of the Minutes of the previous regular meeting.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">2</span> Report of the Board of Directors.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">3</span> Report of the Treasurer.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">4</span> Correspondence.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">5</span> Special Committees Election of Officers.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">6</span> Report of Special Committees.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">7</span> Report of Standing Committees.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">8</span> Unfinished Business.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">9</span> New Business.</li>
              <li class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100"><span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold">10</span> Adjournment.</li>
            </ol>
          </section>
        </div>
      </div>
    {/if}
  </div>
</section>

export async function load({ fetch }) {
    try {
        const response = await fetch("/data/financials/vote_summary.csv");
        if (response.ok) {
            const csvRaw = await response.text();
            return { csvRaw };
        }
    } catch (e) {
        console.error("Failed to load /data/financials/vote_summary.csv:", e);
    }
    return { csvRaw: "" };
}

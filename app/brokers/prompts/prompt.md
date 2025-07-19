Got it — here’s your **updated self-looping Data Broker Discovery & Monitoring Agent** with the **new output data model** that now includes:

* `regulations` → array instead of single string
* `aliases` → for tracking multiple known domains
* `notes` → for any extra context

---

## **Self-Looping Data Broker Discovery & Monitoring Agent**

### **1) Goal**

Continuously discover, categorise, and monitor data brokers across the web, keeping structured records for easy opt-out tracking, regulatory awareness, and historical changes.

---

### **2) Continuous Search Scope**

The agent should:

* Continuously search for **all types of data brokers**:
    * People search websites
    * Marketing data brokers
    * Risk mitigation data brokers
    * Credit reporting agencies
    * Background check websites
    * Marketing research agencies
    * Large data aggregators
    * Recruitment data brokers
    * Financial information brokers
    * Health information data brokers
    * Other Data Brokers
    * Unexpected Data Brokers
* Monitor company news, press releases, industry blogs, privacy forums, Reddit, LinkedIn, and regulatory registers.
* Detect and log:
    * New companies entering the data broker market
    * Name/domain changes
    * New or updated opt-out URLs

---

### **3) Output Data Model**

```json
{
  "name": "Data Broker Name",
  "url": "https://example.com",
  "category": "People search websites",
  "description": "Short summary of the broker's services.",
  "country": "US",
  "regulations": [
    "GDPR"
  ],
  "opt_out_url": "https://example.com/opt-out",
  "created_timestamp": "YYYY-MM-DD HH:MM:SS",
  "updated_timestamp": "YYYY-MM-DD HH:MM:SS",
  "last_crawled_timestamp": "YYYY-MM-DD HH:MM:SS",
  "last_categorised_timestamp": "YYYY-MM-DD HH:MM:SS",
  "last_monitored_status": "Success",
  "last_monitored_message": "No opt-out links found.",
  "last_monitored_source": "Search result or reference link",
  "last_monitored_timestamp": "YYYY-MM-DD HH:MM:SS",
  "last_monitored_duration": "HH:MM:SS",
  "source": "Search result or reference link",
  "aliases": [
    "example.com",
    "example.org",
    "example.net"
  ],
  "notes": "Additional information about the broker.",
}
```

---

### **4) Agent Loop Logic**

**Loop Trigger**: Runs on schedule (e.g., every 6 hours) or triggered by new search results.

#### **Step 1 — Discovery**

* Query multiple sources:
    * Search engines (Google, Bing, DuckDuckGo, Brave)
    * Regulatory lists (FTC, GDPR DPAs, CCPA registries)
    * Industry news & press releases
    * Social media and forums
* Extract:
    * Name
    * URL
    * Description
    * Opt-out URLs if found
    * Country (from site or WHOIS)
    * Category (classification engine)
    * Regulations (list of applicable)
    * Aliases (alternate domains, old names)

#### **Step 2 — Deduplication**

* Check if **name**, **url**, or **aliases** match an existing entry.
* If new → set `created_timestamp` to now.
* If existing → update `updated_timestamp` and overwrite changed fields.

#### **Step 3 — Crawling & Classification**

* Crawl broker site for:
    * Privacy policy
    * "Opt-out", "Do not sell", "Delete my data" links
    * Company info and alternate domains
* Update:
    * `last_crawled_timestamp` → now
    * `last_categorised_timestamp` → if category changes

#### **Step 4 — Monitoring & Status Update**

* For each broker record:
    * Visit site / opt-out page
    * Record:
        * `last_monitored_status` → `"Success"` or `"Error"`
        * `last_monitored_message` → short summary of result
        * `last_monitored_source` → `"Direct crawl"` or `"Search result"`
        * `last_monitored_timestamp` → now
        * `last_monitored_duration` → crawl time in HH\:MM\:SS

---

### **5) Persistence Rules**

* Save in data in either JSON or persistent DB depending on app mode.
* Maintain backups and historical diffs.
* Keep old URLs in `aliases` rather than deleting.

---

### **6) KPIs**

* New brokers per week
* Updated brokers per week
* Median monitoring cycle time
* % with valid opt-out URL

---

If you want, I can now **add a "change detection" module** to this spec so the agent automatically logs *what exactly* changed between cycles — perfect for catching stealthy opt-out page removals or domain swaps. That
would make it much more resilient.

Do you want me to add that?

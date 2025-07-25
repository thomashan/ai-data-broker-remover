# ai-data-broker-remover

Opensource AI data broker removal service.

## Use AI agents and RAG to remove personal data

This project is to experiment with removing data from the data brokers using AI agents and RAG.

### Prerequisites

Before you begin, ensure you have `make` installed on your system. Most Unix-like operating systems (Linux, macOS) come with `make` pre-installed.
## Project setup

Since this project is in alpha we suggest using a sandboxed Python environment to explore its possibilities.

### Step 1: Install Miniforge

This project uses Miniforge for managing Python environments. To install it, run:

```bash
make setup
```

This command will check if Miniforge is already installed and, if not, will install it using the appropriate method for your operating system.

After the installation is complete, you **must** restart your terminal or run the following command to initialize the conda environment in your current shell session:

```bash
export PATH="$HOME/miniforge3/bin:$PATH" && conda init && eval "$$(conda shell.bash hook)"
```

### Step 2: Create the Conda Environment

Once you have restarted your terminal or run the `eval` command, you can create the conda environment for this project:

```bash
make create-conda-env
```

This will create a conda environment named `ai-data-broker-remover` with Python 3.13.

### Step 3: Activate the Conda Environment

To activate the newly created environment, run:

```bash
conda activate ai-data-broker-remover
```

### Supported Platforms
- **macOS:** Uses Homebrew (brew install --cask miniforge)
- **Linux:** Downloads and installs from GitHub releases for x86_64 and aarch64 architectures.
  - Ubuntu/Debian (apt-get)
  - RHEL/CentOS (yum)
  - Fedora (dnf)
  - Arch Linux (pacman)
  - openSUSE (zypper)

## Data Broker Remover

From https://deletemyinfo.com/best-data-removal-services-of-2025/

| Rank | Service Name        | Best For                                 | Pricing Starts At |
|------|---------------------|------------------------------------------|-------------------|
| 1    | DeleteMyInfo        | Full coverage + human verification       | $120/year         |
| 2    | DeleteMe            | Custom opt-outs and privacy advisor      | $129/year         |
| 3    | Incogni             | Automated removal from marketing brokers | $89.88/year       |
| 4    | Optery              | Predictive link scanning & screenshots   | $39/year          |
| 5    | Onerep              | Google search cleanup                    | $99.95/year       |
| 6    | Kanary              | Opt-out templates & reporting            | $179.88/year      |
| 7    | Privacy Bee         | Non-public broker removals               | $197/year         |
| 8    | EasyOptOuts         | Budget-friendly service                  | $19.99/year       |
| 9    | PrivacyPros         | Genealogy & voter site removals          | $299.99/year      |
| 10   | Confidently         | Variety of site types                    | $10/month         |
| 11   | Erase Me            | Visual exposure reports                  | $127/year         |
| 12   | DataSeal            | Data breach alerts                       | $99.99/year       |
| 13   | HelloPrivacy        | Simple dashboard + breach alerts         | $99.99/year       |
| 14   | PurePrivacy         | Social media privacy audit               | $69.99/year       |
| 15   | MyDataRemoval       | Custom report delivery options           | $99.96/year       |
| 16   | PrivacyHawk         | Email inbox scanning                     | $74.99/year       |
| 17   | Guaranteed Removals | Pay-after-removal model                  | Custom Quote      |
| 18   | ReputationDefender  | Reputation report card                   | $1,000+/year      |
| 19   | BrandYourself       | DIY reputation cleanup                   | $299.99/year      |
| 20   | Aura                | Digital security suite                   | $3/month          |
| 21   | Malwarebytes        | Antivirus + privacy                      | $9.99/month       |
| 22   | IDX                 | Identity theft recovery + removal        | $139.92/year      |
| 23   | Voiply              | Phone + data scrub bundle                | $69.95/year       |
| 24   | McAfee Cleanup      | Data removal + antivirus                 | $199.99/year      |
| 25   | Avast BreachGuard   | Simple removal + breach alerts           | $43.99/year       |

## DeleteMyInfo

**Specs to Emulate DeleteMyInfo:**

1. **Full Coverage Approach**: Target comprehensive list of 750+ data brokers including major and obscure sites
2. **Human Verification**: Implement manual verification step for each removal request
3. **Custom Opt-outs**: Create personalized removal requests based on individual profiles
4. **Quarterly Reports**: Generate detailed progress reports every 3 months
5. **Priority Targeting**: Focus on high-risk brokers first (background check sites, people search engines)
6. **Legal Compliance**: Ensure all requests comply with CCPA, GDPR, and state privacy laws
7. **Follow-up System**: Automated follow-up emails for non-responsive brokers
8. **Screenshot Documentation**: Capture before/after screenshots as proof of removal

## DeleteMe

**Specs to Emulate DeleteMe:**

1. **Custom Opt-outs**: Personalized removal requests tailored to individual data footprints
2. **Privacy Advisor**: Provide expert guidance on privacy best practices
3. **Quarterly Monitoring**: Regular scans to detect if data reappears
4. **Comprehensive Database**: Target 600+ data broker sites
5. **Legal Compliance**: CCPA and GDPR compliant removal processes
6. **Progress Tracking**: Real-time dashboard showing removal progress
7. **Expert Support**: Access to privacy specialists for complex cases
8. **Continuous Monitoring**: Ongoing surveillance for new data appearances

## Incogni

**Specs to Emulate Incogni:**

1. **Automated Removal**: Fully automated system for marketing broker removals
2. **Marketing Broker Focus**: Target data brokers used primarily for marketing purposes
3. **Bulk Processing**: Process multiple removal requests simultaneously
4. **GDPR/CCPA Requests**: Leverage privacy laws for faster removal
5. **Regular Scans**: Monthly automated scans for new data appearances
6. **Simple Dashboard**: Clean interface showing removal status
7. **Email Automation**: Automated email templates for different broker types
8. **Progress Reporting**: Regular updates on removal progress

## Optery

**Specs to Emulate Optery:**

1. **Predictive Link Scanning**: AI-powered detection of potential data broker profiles
2. **Screenshot Capture**: Automatic screenshots of profiles before removal
3. **Smart Scanning**: Predictive algorithms to find hidden profiles
4. **Budget Tiers**: Multiple service levels (Essential, Professional, Ultimate)
5. **Regular Monitoring**: Continuous scanning for new data appearances
6. **Profile Matching**: Advanced algorithms to match user profiles across sites
7. **Removal Automation**: Automated submission of removal requests
8. **Detailed Reports**: Comprehensive removal reports with visual proof

## Onerep

**Specs to Emulate Onerep:**

1. **Google Search Cleanup**: Focus on removing data that appears in Google search results
2. **Search Result Monitoring**: Regular monitoring of search results for personal data
3. **Profile Removal**: Target people search engines and background check sites
4. **Search Optimization**: Techniques to push down negative search results
5. **Monthly Reports**: Regular updates on search result improvements
6. **Automated Scanning**: Continuous monitoring of search engine results
7. **Removal Verification**: Confirmation that data no longer appears in searches
8. **Privacy Dashboard**: User-friendly interface showing search result status

## Kanary

**Specs to Emulate Kanary:**

1. **Opt-out Templates**: Pre-built templates for different types of data brokers
2. **Comprehensive Reporting**: Detailed reports on removal progress and status
3. **Template Library**: Extensive collection of removal request templates
4. **Legal Compliance**: Templates that comply with various privacy regulations
5. **Progress Tracking**: Real-time updates on removal request status
6. **Broker Database**: Comprehensive list of data brokers with removal procedures
7. **Automated Follow-ups**: System for following up on pending requests
8. **Custom Templates**: Ability to create custom templates for unique situations

## Privacy Bee

**Specs to Emulate Privacy Bee:**

1. **Non-public Broker Focus**: Target lesser-known and non-public data brokers
2. **Deep Web Scanning**: Search for data on non-indexed and private databases
3. **Specialized Removal**: Handle complex removal cases requiring special procedures
4. **B2B Data Brokers**: Focus on business-to-business data aggregators
5. **Advanced Techniques**: Use sophisticated methods for hard-to-remove data
6. **Privacy Consulting**: Expert advice on complex privacy situations
7. **Custom Solutions**: Tailored approaches for unique data exposure cases
8. **Confidential Handling**: Secure processing of sensitive information

## EasyOptOuts

**Specs to Emulate EasyOptOuts:**

1. **Budget-Friendly Service**: Cost-effective solution for basic data removal
2. **Essential Coverage**: Target most common and high-impact data brokers
3. **Simple Process**: Streamlined removal process with minimal user input
4. **Basic Monitoring**: Regular checks for data reappearance
5. **Email Templates**: Standard email templates for common broker types
6. **Progress Updates**: Regular notifications on removal progress
7. **Core Brokers**: Focus on 50-100 most important data broker sites
8. **Self-Service Options**: Tools for users to handle some removals themselves

## PrivacyPros

**Specs to Emulate PrivacyPros:**

1. **Genealogy Site Removal**: Specialized removal from ancestry and genealogy websites
2. **Voter Database Removal**: Focus on removing data from voter registration databases
3. **Public Record Cleanup**: Target government and public record databases
4. **Specialized Databases**: Handle niche and specialized data collection sites
5. **Research Databases**: Remove data from academic and research databases
6. **Historical Data**: Address long-standing data that's difficult to remove
7. **Custom Research**: Investigate unique data exposure situations
8. **Specialized Expertise**: Deep knowledge of specific database types

## Confidently

**Specs to Emulate Confidently:**

1. **Variety Coverage**: Target diverse types of data broker sites
2. **Flexible Service**: Adaptable approach for different user needs
3. **Multi-Site Scanning**: Search across various types of databases
4. **Comprehensive Approach**: Don't limit to specific broker categories
5. **Regular Monitoring**: Ongoing surveillance across multiple site types
6. **Adaptive Strategy**: Adjust tactics based on site-specific requirements
7. **Broad Database**: Include mainstream and niche data brokers
8. **Versatile Templates**: Flexible removal request formats

## Erase Me

**Specs to Emulate Erase Me:**

1. **Visual Exposure Reports**: Detailed visual reports showing data exposure
2. **Screenshot Documentation**: Comprehensive before/after visual proof
3. **Visual Dashboard**: Image-rich interface showing removal progress
4. **Exposure Mapping**: Visual representation of data spread across sites
5. **Photo Documentation**: Capture and document all found data instances
6. **Visual Verification**: Image-based confirmation of successful removals
7. **Report Generation**: Create visual reports for user review
8. **Timeline Visualization**: Show removal progress over time visually

## DataSeal

**Specs to Emulate DataSeal:**

1. **Data Breach Alerts**: Real-time notifications of data breaches affecting users
2. **Breach Monitoring**: Continuous monitoring of known breach databases
3. **Alert System**: Immediate notifications when user data appears in breaches
4. **Breach Response**: Automated actions when breaches are detected
5. **Dark Web Monitoring**: Search for user data on dark web marketplaces
6. **Identity Protection**: Comprehensive protection beyond just broker removal
7. **Threat Intelligence**: Use threat data to predict potential exposures
8. **Proactive Alerts**: Early warning system for potential data exposure

## HelloPrivacy

**Specs to Emulate HelloPrivacy:**

1. **Simple Dashboard**: Clean, easy-to-use interface for tracking progress
2. **Breach Alerts**: Notifications when user data appears in breaches
3. **Streamlined Process**: Simplified removal workflow with minimal user input
4. **Progress Tracking**: Clear indicators of removal status and progress
5. **User-Friendly Reports**: Easy-to-understand progress reports
6. **Automated Monitoring**: Background scanning for new data appearances
7. **Essential Features**: Focus on core functionality without complexity
8. **Regular Updates**: Consistent communication about removal progress

## PurePrivacy

**Specs to Emulate PurePrivacy:**

1. **Social Media Privacy Audit**: Comprehensive review of social media privacy settings
2. **Platform Analysis**: Examine privacy settings across multiple social platforms
3. **Privacy Recommendations**: Suggest optimal privacy configurations
4. **Social Media Monitoring**: Track mentions and data sharing on social platforms
5. **Privacy Score**: Generate privacy ratings based on current settings
6. **Configuration Assistance**: Help users optimize their privacy settings
7. **Social Media Cleanup**: Remove unwanted public information from profiles
8. **Platform Integration**: Direct integration with major social media platforms

## MyDataRemoval

**Specs to Emulate MyDataRemoval:**

1. **Custom Report Delivery**: Flexible options for receiving progress reports
2. **Personalized Reporting**: Tailored reports based on user preferences
3. **Multiple Formats**: Offer reports in various formats (PDF, email, dashboard)
4. **Scheduled Reports**: Allow users to set custom reporting schedules
5. **Detailed Analytics**: Comprehensive data on removal progress and success rates
6. **Custom Dashboards**: User-configurable interfaces for tracking progress
7. **Export Options**: Allow users to export their data and reports
8. **Flexible Communication**: Multiple channels for updates and notifications

## PrivacyHawk

**Specs to Emulate PrivacyHawk:**

1. **Email Inbox Scanning**: Analyze emails for privacy risks and data sharing
2. **Email Monitoring**: Continuous scanning of user email accounts
3. **Privacy Risk Detection**: Identify potential privacy threats in emails
4. **Unsubscribe Management**: Automated unsubscribing from unwanted lists
5. **Email Analytics**: Analyze email patterns for privacy risks
6. **Phishing Detection**: Identify potential phishing and scam emails
7. **Data Request Identification**: Find emails containing data requests or confirmations
8. **Email-Based Removal**: Use email analysis to identify removal opportunities

## Guaranteed Removals

**Specs to Emulate Guaranteed Removals:**

1. **Pay-After-Removal Model**: Payment only after successful data removal
2. **Results-Based Pricing**: Pricing tied to actual removal success
3. **Performance Guarantee**: Commit to achieving specific removal results
4. **Success Metrics**: Clear definitions of successful removal
5. **Quality Assurance**: Rigorous verification of removal completion
6. **Risk-Free Service**: No upfront payment required from users
7. **Accountability Focus**: Strong emphasis on delivering promised results
8. **Transparent Pricing**: Clear cost structure based on actual results

## ReputationDefender

**Specs to Emulate ReputationDefender:**

1. **Reputation Report Card**: Comprehensive analysis of online reputation
2. **Online Reputation Management**: Full-service reputation monitoring and improvement
3. **Content Removal**: Remove negative or unwanted online content
4. **SEO Optimization**: Improve positive content visibility in search results
5. **Monitoring Services**: Continuous tracking of online mentions and content
6. **Crisis Management**: Rapid response to reputation threats
7. **Content Creation**: Generate positive content to improve online presence
8. **Executive Protection**: Specialized services for high-profile individuals

## BrandYourself

**Specs to Emulate BrandYourself:**

1. **DIY Reputation Cleanup**: Self-service tools for reputation management
2. **User-Friendly Tools**: Easy-to-use interface for non-technical users
3. **Step-by-Step Guidance**: Clear instructions for reputation improvement
4. **Reputation Monitoring**: Track changes in online reputation over time
5. **Content Strategy**: Help users create positive online content
6. **Search Result Optimization**: Tools to improve search result rankings
7. **Educational Resources**: Training materials on reputation management
8. **Progressive Approach**: Gradual improvement strategies

## Aura

**Specs to Emulate Aura:**

1. **Digital Security Suite**: Comprehensive protection including identity theft, VPN, and antivirus
2. **Identity Monitoring**: Track use of personal information across the web
3. **Financial Monitoring**: Monitor bank accounts and credit reports for suspicious activity
4. **VPN Integration**: Built-in VPN for secure browsing
5. **Antivirus Protection**: Malware and virus protection alongside privacy services
6. **Family Plans**: Protection for entire families with multiple profiles
7. **Insurance Coverage**: Identity theft insurance included
8. **24/7 Support**: Round-the-clock customer support

## Malwarebytes

**Specs to Emulate Malwarebytes:**

1. **Antivirus + Privacy**: Combined malware protection and privacy services
2. **Malware Detection**: Advanced threat detection and removal
3. **Privacy Protection**: Block tracking and protect personal data
4. **Real-Time Protection**: Continuous monitoring for threats and privacy risks
5. **Web Protection**: Safe browsing with automatic threat blocking
6. **Anti-Exploit**: Protection against zero-day exploits
7. **Ransomware Protection**: Specialized defense against ransomware attacks
8. **Privacy Dashboard**: Centralized control over privacy settings

## IDX

**Specs to Emulate IDX:**

1. **Identity Theft Recovery**: Comprehensive support for identity theft victims
2. **Data Removal**: Remove personal information from data broker sites
3. **Credit Monitoring**: Track changes to credit reports and scores
4. **Recovery Services**: Full-service identity restoration after theft
5. **Insurance Coverage**: Identity theft insurance protection
6. **Expert Support**: Access to identity theft recovery specialists
7. **Legal Assistance**: Legal support for identity theft cases
8. **Restoration Services**: Complete identity restoration after compromise

## Voiply

**Specs to Emulate Voiply:**

1. **Phone + Data Bundle**: Combined phone privacy and data removal services
2. **Phone Number Protection**: Remove phone numbers from data broker sites
3. **Call Blocking**: Block unwanted calls and spam
4. **Number Monitoring**: Track where phone numbers appear online
5. **Telemarketing Opt-out**: Remove numbers from telemarketing lists
6. **Caller ID Protection**: Prevent number from appearing in caller ID databases
7. **SMS Protection**: Block unwanted text messages
8. **Comprehensive Phone Privacy**: Full protection for phone-related data

## McAfee Cleanup

**Specs to Emulate McAfee Cleanup:**

1. **Data Removal + Antivirus**: Combined security and privacy protection
2. **Personal Data Cleanup**: Remove personal information from online databases
3. **Security Software**: Full antivirus and anti-malware protection
4. **Identity Protection**: Monitor for identity theft and fraud
5. **Safe Browsing**: Web protection against malicious sites
6. **Password Manager**: Secure password storage and generation
7. **VPN Service**: Secure browsing with encrypted connections
8. **Comprehensive Suite**: All-in-one security and privacy solution

## Avast BreachGuard

**Specs to Emulate Avast BreachGuard:**

1. **Simple Removal Process**: Streamlined approach to data broker removal
2. **Breach Alerts**: Immediate notifications of data breaches
3. **Automatic Scanning**: Regular automated scans for personal data
4. **Easy Interface**: User-friendly dashboard for tracking progress
5. **Quick Setup**: Fast onboarding and initial scan process
6. **Breach Monitoring**: Continuous monitoring of breach databases
7. **Basic Reporting**: Simple progress reports and notifications
8. **Affordable Protection**: Cost-effective privacy protection solution

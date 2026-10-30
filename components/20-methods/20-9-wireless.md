# 20.9 · Wireless Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## A radio signal is not a permission boundary

Wireless testing asks which nearby devices can see or join a network, which identities and configurations govern that access, and what a successful connection can actually reach. Those are three different questions. Seeing an SSID does not establish a rogue device; capturing an authentication exchange does not establish a recovered secret; joining a guest network does not establish access to a protected system.

Use [§20.1](20-1-method-framework.md) as the umbrella method and the engagement's scope and rules records (§10.1/10.2/10.4). §20.5 owns network reach and §20.10 owns network admission controls after association. Application/API behavior routes to §20.2/20.3. A wireless observation does not authorize testing an adjacent host, identity system, or business application.

[NIST SP 800-153](https://www.nist.gov/publications/guidelines-securing-wireless-local-area-networks-wlans) supplies a WLAN lifecycle and security reference. [RFC 9190](https://datatracker.ietf.org/doc/html/rfc9190) is a protocol reference for EAP-TLS 1.3 when applicable. The [OWASP Wi-Fi Security Testing Guide](https://owasp.org/projects/wi-fi-security-testing-guide?tab=main) is an incubating community project, not a certification or substitute for the observed configuration. Use the currently applicable PCI DSS edition only when a payment-card requirement is in scope; a method test does not itself establish compliance.

## Set the site boundary before turning on a transmitter

Record the exact sites, floors or zones; authorized SSIDs/BSSIDs and owners; client populations; bands/channels; authentication modes; back-end identity services; expected segmentation; and the approved source position. Identify the approved test accounts and devices. A nearby network bearing a familiar name is still an unverified candidate until ownership is established.

The rules should separately authorize passive discovery, association, credential testing, active impersonation, client steering/deauthentication, denial-of-service, segmentation probes, and optional Bluetooth/IoT testing. Specify test windows, power/rate ceilings, client-impact limits, radio/regulatory obligations, a live site contact, stop signal and rollback. Guest, production, medical/operational, and payment environments may have different ceilings. If a test would touch uninvolved clients or neighboring networks, stop and re-scope.

Prepare a known-good client and adapter configuration, a time-synchronized capture path, and an evidence store with access, retention and redaction controls. Record firmware/driver and analyzer versions with the result. Tool availability is not authority to transmit. Avoid collecting real passwords or payload data when a test fixture answers the question.

## Build the map, then test the decisions

Start with passive inventory: observed SSID/BSSID, channel/band, security advertisement, signal/location, timestamps, and candidate client association. Reconcile observations against the owner-maintained AP inventory and site survey. An unlisted BSSID, duplicate SSID, unexpected band or weak-signal footprint is an **investigation lead**, not proof of a rogue AP. Confirm asset ownership and physical/location context before describing it as unauthorized.

For every active test, preserve a small evidence row:

| Field | Record |
|---|---|
| Starting state | Site/zone, device, radio configuration, test identity, time, approved target and band. |
| Expected rule | Which client should join, which authentication and server trust should be required, and which destinations should be reachable. Name the owner/policy source. |
| Safe contrast | A known-permitted case and a bounded negative case changing one relevant condition. |
| Observation | Association/authentication result, relevant protocol trace or configuration, exact destination/response, and independent corroboration. |
| Limit | What was inferred, not exercised, outside scope, or stopped for safety. |
| Disposition | Owner/reviewer decision, protected artifact pointer, remediation direction and retest condition. |

The method below is a menu, not a mandate. Select each card by the actual technology and authorization; record “not applicable” or “not tested” rather than silently omitting it.

| Test family | Question and bounded check | Evidence and interpretation bar |
|---|---|---|
| Authorized inventory and configuration | Do observed radios and advertised security modes match the owner inventory and intended site policy? Confirm anomalies with the AP owner and physical/site evidence. | A broadcast alone establishes only an observation. Asset inventory, management-plane record or controlled location check is needed for ownership. |
| WPA2-Personal | Can an authorized test client join with the intended shared secret, and is a deliberately invalid secret rejected? If a password-strength exercise is explicitly approved, use the captured exchange only within the agreed offline/time ceiling. | A captured handshake or PMKID is **not** a recovered PSK or network access. Record the actual recovery result, key-handling boundary and remediation decision. |
| WPA2-Enterprise / 802.1X | Does the intended identity and EAP policy permit the right test account and reject an unauthorized one? Inspect client server-trust configuration and RADIUS/identity-service records with the owner. | An observed response or configuration weakness is not automatically a recovered credential or directory access. Prove the specific client and server behavior. |
| EAP-TLS and certificates | Does the client validate the expected server identity and trust chain, and is the test credential bound to the intended identity? Use owner-approved client profiles and a bounded negative trust case. | A public client certificate is not a private key. Missing server validation does not prove private-key extraction or session compromise; those require separate evidence. |
| WPA3/SAE and transition | Which modes do the AP and representative clients actually negotiate? Does a client fall back to an allowed WPA2 path and under which configuration? | Transition mode permits coexistence; it is not by itself a successful downgrade attack. Separate capability, negotiation, configuration and demonstrated exposure. SAE does not inherently provide per-user identity. |
| Open, OWE and captive portal | What protection exists before portal acceptance, and can the approved client reach destinations contrary to the stated policy? Inspect transport and portal behavior without collecting uninvolved users' traffic. | Portal appearance is not proof of network encryption, and encryption is not proof of authorization. Record the actual path and data boundary. |
| Rogue/evil-twin scenario | If explicitly authorized, can a controlled test radio attract the named test client, and what does that client reveal or trust? Keep power, location and client allowlist narrow. | Do not equate an SSID match with exploitation. Record association, certificate prompts and any disclosed test-only data separately. Stop before uninvolved clients are affected. |
| WPS and onboarding | Is WPS or another onboarding route enabled where policy forbids it, and does a bounded negative attempt demonstrate a bypass? | Configuration evidence and an observed successful join are different claims. Do not run broad PIN attempts without a separate ceiling. |
| Guest/IoT segmentation | From an authorized associated test device, can the named protected destination be reached by the disallowed protocol/action? Compare with a permitted path and owner network policy. | Internal reach is not automatically a PCI or enterprise segmentation failure. Name the expected boundary and demonstrate the prohibited flow. |
| Management plane | Can a lower-trust wireless position access AP/controller administration, configuration or secrets beyond its role? Use an owner-approved test identity and benign read/negative case. | Seeing a login page is not control-plane compromise. Any change action needs an explicit ceiling and rollback. |
| Modern-band and peripheral overlay | For deployed 6 GHz, Wi-Fi 6E/7, BLE or IoT radios, identify actual devices, protocol modes, identity and segmentation assumptions; scope separately if materially different. | Do not infer a vulnerability from a feature name or version. Verify device/firmware-specific behavior and applicable guidance. |

## Keep chain steps attached to their proof

The method offers useful path families: shared secret to association, Enterprise identity to network access, client trust to impersonation risk, rogue radio to portal interaction, unauthorized AP to network position, and guest/IoT network to protected destination. Treat them as hypotheses that help choose the next check—not prewritten findings.

| State | Wireless example | Permitted claim |
|---|---|---|
| Observed | A test client sees an unexpected BSSID advertising an authorized SSID. | The broadcast, location, time and advertised configuration; ownership unresolved. |
| Corroborated | Inventory and owner review identify the BSSID as an unauthorized device. | The unauthorized device and its demonstrated connection/upstream path, if tested. |
| Demonstrated | A named test client associates under an approved scenario and reaches a named disallowed fixture. | The exact client, identity, route and prohibited action. |
| Conditional / untested | A next step might use a recovered secret, a real employee client, or a production identity system outside the rules. | The missing proof and a separate scope request—not a claimed compromise. |

**Synthetic example.** A guest SSID is expected to reach the internet but not an internal test fixture. A permitted client associates, confirms ordinary internet access, then sends one owner-approved request to the fixture. If the fixture responds across the prohibited boundary and the route/policy are corroborated, report the tested guest-to-fixture path. Do not report “all internal systems exposed,” and do not call it a PCI boundary failure unless that exact boundary is in scope and evidenced.

## Report, restore, and hand off

For each finding, give the expected control, tested device/client/identity and location, protocol/configuration evidence, bounded reproduction, actual effect, competing explanations, limit, severity rationale, remediation direction and retest. Do not assign Critical/High from the test family alone. A configuration gap and a demonstrated exploit path may warrant different treatments. Keep packet captures, credentials and device identifiers in protected custody; use redacted reporting derivatives.

Close with owner-verified cleanup of test radios, access points, accounts, keys, client profiles and any temporary controller changes. Route wider network reach to §20.5/20.10 and application behavior to its own method with a fresh authorization check. Preserve the handoff from radio observation through identity and destination so the next team can see which edges were actually tested.

Inventory comparison, capture triage and protocol/configuration correlation could reduce manual sorting. These are possibilities for a future, bounded automation design—not deployed testing capabilities. Active transmission, credential work, client impact, finding validation and final disposition remain bound to the same rules and named human owner.

The useful output is a scoped account of who or what could join, under which trust decision, and what that position could reach. It leaves the untested paths visible instead of filling them in with a tool's confidence—or with our own.

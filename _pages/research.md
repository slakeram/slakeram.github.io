---
layout: single
title: ""
permalink: /research/
author_profile: false
---

<div class="kolam-page-marker kolam-research" aria-hidden="true"></div>

<div class="botanical-intro">
  <p class="botanical-eyebrow">RESEARCH PROGRAM</p>
  <h1>Reconstructing the ecological interactions of ancient forests</h1>
  <p>Plant–arthropod interactions and the evolution of terrestrial ecosystems across deep time.</p>
</div>

<div class="research-story">

  <section class="research-story-opening" aria-labelledby="research-intro">
    <h2 id="research-intro">Understanding ancient ecosystems</h2>
    <p>Plants and arthropods have shaped terrestrial ecosystems for hundreds of millions of years. Through feeding and decomposition, these interactions influence how ecosystems function and respond to environmental change. Yet much of their early evolutionary history remains poorly understood.</p>
    <p>Fossil feeding traces from Pennsylvanian peat-forming forests provide a window into how plants and arthropods interacted in ancient ecosystems. Research combining these traces with modern ecological comparisons examines the organization of ancient food webs, patterns of plant-resource use, and changes in ecological relationships through time.</p>
  </section>

  <section aria-labelledby="fossil-evidence">
    <p class="research-story-eyebrow">THE FOSSIL EVIDENCE</p>
    <h2 id="fossil-evidence">Windows into ancient ecosystems</h2>
    <div class="research-story-copy">
      <h3>Coal balls: Preserving ancient forests</h3>
      <p>Coal balls formed when mineral-rich water entered ancient peat deposits and minerals, commonly calcium carbonate, precipitated around buried plant material. This early mineralization preserved delicate tissues before they were compacted and altered during coal formation.</p>
      <p>As a result, coal balls can preserve roots, stems, leaves, and other plant organs in remarkable anatomical detail. They provide a rare glimpse into the plants of Pennsylvanian peat forests and the organisms that interacted with them.</p>
    </div>
    <div class="coal-book-gallery" data-coal-book-gallery aria-label="Phillips Coal Ball Collection image gallery">
      <div class="coal-book-heading">
        <p class="research-story-eyebrow">ARCHIVAL PLATES</p>
        <h4>Coal-ball plant anatomy</h4>
      </div>
      <figure class="coal-book-figure">
        <div class="coal-book-stage">
          <a class="coal-book-enlarge" href="{{ '/images/TC-Ferns%20page%201.jpeg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open current archival plate at full resolution">
            <img class="coal-book-image" src="{{ '/images/TC-Ferns%20page%201.jpeg' | relative_url }}" alt="Archival coal-ball plate 1 of 5, examples 1–3, Phillips Coal Ball Collection" loading="lazy">
          </a>
        </div>
        <figcaption class="coal-book-caption">Material from the <strong>Phillips Coal Ball Collection</strong>.</figcaption>
      </figure>
      <nav class="coal-book-controls" aria-label="Navigate archival plates">
        <button class="coal-book-prev" type="button" aria-label="Previous plate">← Previous</button>
        <span class="coal-book-count" role="status" aria-live="polite">Plate 1 of 5 · Examples 1–3</span>
        <button class="coal-book-next" type="button" aria-label="Next plate">Next →</button>
      </nav>
    </div>
    <script>
    (function () {
      const root = document.querySelector('[data-coal-book-gallery]');
      if (!root) return;
      const base = {{ '/images/' | relative_url | jsonify }};
      const pages = [
        ['TC-Ferns page 1.jpeg', '1–3'],
        ['TC-Ferns page 2jpeg.jpeg', '4–5'],
        ['TC-Ferns page 3.jpeg', '6–7'],
        ['TC-Ferns page 4.jpeg', '8–9'],
        ['TC-Ferns page 5.jpeg', '10']
      ];
      let index = 0;
      let busy = false;
      const image = root.querySelector('.coal-book-image');
      const link = root.querySelector('.coal-book-enlarge');
      const count = root.querySelector('.coal-book-count');
      const prev = root.querySelector('.coal-book-prev');
      const next = root.querySelector('.coal-book-next');
      const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
      function updateButtons() {
        prev.disabled = busy || index === 0;
        next.disabled = busy || index === pages.length - 1;
      }
      function showPage(direction) {
        const target = index + direction;
        if (busy || target < 0 || target >= pages.length) return;
        busy = true;
        updateButtons();
        const file = pages[target][0];
        const url = base + encodeURIComponent(file);
        const incoming = new Image();
        incoming.onload = function () {
          const animate = !reduceMotion.matches;
          if (animate) image.classList.add(direction > 0 ? 'coal-book-turn-next' : 'coal-book-turn-prev');
          window.setTimeout(function () {
            index = target;
            image.src = url;
            image.alt = 'Archival coal-ball plate ' + (index + 1) + ' of 5, examples ' + pages[index][1] + ', Phillips Coal Ball Collection';
            link.href = url;
            count.textContent = 'Plate ' + (index + 1) + ' of 5 · Examples ' + pages[index][1];
            image.classList.remove('coal-book-turn-next', 'coal-book-turn-prev');
            if (animate) {
              image.classList.add('coal-book-arrive');
              window.setTimeout(function () { image.classList.remove('coal-book-arrive'); busy = false; updateButtons(); }, 360);
            } else { busy = false; updateButtons(); }
          }, animate ? 360 : 0);
        };
        incoming.onerror = function () {
          busy = false;
          updateButtons();
          count.textContent = 'Plate image unavailable; please check the uploaded filename.';
        };
        incoming.src = url;
      }
      prev.addEventListener('click', function () { showPage(-1); });
      next.addEventListener('click', function () { showPage(1); });
      root.addEventListener('keydown', function (event) {
        if (event.key === 'ArrowLeft') { event.preventDefault(); showPage(-1); }
        if (event.key === 'ArrowRight') { event.preventDefault(); showPage(1); }
      });
      updateButtons();
    }());
    </script>
    <div class="research-story-coprolites">
      <div class="research-story-copy">
        <h3>Coprolites: Evidence of ancient feeding</h3>
        <p>Coprolites are fossilized fecal material that preserve evidence of what ancient organisms consumed. Their shapes, internal structures, and preserved plant fragments provide clues about feeding behavior that would otherwise be difficult to recognize in the fossil record.</p>
        <p>They are particularly valuable for studying small arthropods whose bodies are rarely preserved. My research draws on more than 6,000 examined coprolites and systematic frameworks for 26 morphotypes to investigate herbivory and detritivory.</p>
      </div>
      <div class="research-story-gallery research-story-coprolite-gallery">
        <figure>
          <img src="{{ '/images/cordaite%20wood%20copro%20mite.png' | relative_url }}" alt="Fossil coprolite and associated mite in cordaite wood" loading="lazy"/>
          <figcaption>Coprolites (indicated by the pink arrows) attributed to oribatid mites preserved within borings in Cordaites wood.</figcaption>
        </figure>
        <figure>
          <img src="{{ '/images/Convolutispora%20matrix%20coprolite.png' | relative_url }}" alt="A coprolite indicated by a pink arrow containing spores from Psaronius tree ferns, Convolutispora, occurring in the peat matrix" loading="lazy"/>
          <figcaption>A coprolite (indicated by a pink arrow) containing spores from <em>Psaronius</em> tree ferns, <em>Convolutispora</em>, occurring in the peat matrix.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section aria-labelledby="network-explainer">
    <p class="research-story-eyebrow">FROM FOSSILS TO ECOLOGY</p>
    <h2 id="network-explainer">Reconstructing ancient food webs</h2>
    <p>Fossils preserve more than individual organisms. They can also provide evidence of the relationships between them. Identifying plant tissues within different coprolite morphotypes helps reveal which resources were consumed and how they were used.</p>
    <p>Bipartite networks help visualize associations between coprolite types and plant resources. These patterns provide a framework for examining resource use, feeding specialization, and the organization of ancient food webs. Potential arthropod producers are inferred from the fossil evidence rather than always directly identified.</p>
    <figure class="research-story-network">
      <img src="{{ '/images/coprolite_network_diagram.svg' | relative_url }}" alt="Simplified schematic connecting potential arthropod producers to coprolite morphotypes or damage types and plant resources" loading="lazy"/>
      <figcaption>Simplified illustration of how fossil feeding evidence can inform food-web reconstruction. Connections are conceptual, not plotted research data.</figcaption>
    </figure>
  </section>

  <section aria-labelledby="research-questions">
    <p class="research-story-eyebrow">RESEARCH QUESTIONS</p>
    <h2 id="research-questions">Three central research questions</h2>

    <article class="research-story-question" id="decomposition">
      <span class="research-story-number">01</span>
      <div>
        <h3>How did arthropods contribute to decomposition in ancient forests?</h3>
        <p>Decomposition is essential to the recycling of organic material, yet the role of arthropods in this process remains poorly understood in ancient peat-forming environments. Coprolites, borings, and other feeding traces provide evidence of how arthropods consumed and processed plant material before burial.</p>
      </div>
    </article>

    <article class="research-story-question" id="specialization">
      <span class="research-story-number">02</span>
      <div>
        <h3>How did arthropods share plant resources in ancient food webs?</h3>
        <p>Not all organisms consume the same resources. Plant tissues preserved within different coprolite morphotypes reveal patterns of resource use and potential feeding specialization. Comparing these associations across fossil assemblages helps reveal how feeding relationships changed as ancient forests evolved.</p>
      </div>
    </article>

    <article class="research-story-question" id="change">
      <span class="research-story-number">03</span>
      <div>
        <h3>How did ancient food webs respond to environmental change?</h3>
        <p>Environmental change can alter not only which organisms inhabit an ecosystem, but also how they interact. Comparisons of fossil plants and feeding traces across environmental transitions, including the Middle–Late Pennsylvanian Floral Transition, help reveal how ecological interactions reorganized during disruption and recovery.</p>
      </div>
    </article>
  </section>

  <section aria-labelledby="modern-ecology">
    <p class="research-story-eyebrow">CONNECTING PAST AND PRESENT</p>
    <h2 id="modern-ecology">Modern ecological comparisons</h2>
    <p>Modern ecosystems offer valuable comparisons for interpreting processes preserved in the fossil record. My ongoing research in the Florida Keys and Everglades examines insect herbivory on mangrove foliage across environmental gradients. Complementary investigations in South Florida wetlands examine plant litter, arthropod activity, and organic-matter accumulation.</p>
    <p>These comparisons connect feeding, decomposition, and resource use in living ecosystems with the long-term history of terrestrial ecological interactions.</p>
    <div class="research-story-gallery">
      <figure><img src="{{ '/images/herbivory%20on%20red%20mangrove.jpg' | relative_url }}" alt="Insect herbivory on a red mangrove leaf" loading="lazy"/><figcaption>Galls and skeletonization of red mangrove foliage</figcaption></figure>
      <figure><img src="{{ '/images/mangrove%20tree.jpg' | relative_url }}" alt="Mangrove tree in a coastal ecosystem" loading="lazy"/><figcaption>Red mangrove (<em>Rhizophora mangle</em>) growing along a shallow coastal shoreline on Lower Matecumbe Key.</figcaption></figure>
    </div>
  </section>

  <section class="research-story-further">
    <p>For a list of publications, visit the <a href="{{ '/publications/' | relative_url }}">Publications page</a>.</p>
  </section>
</div>

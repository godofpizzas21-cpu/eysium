/**
 * Stars.
 *
 * Deterministic, so the sky is the same on every visit, and dim: Elysium's
 * dark-sky standards are the reason its aurora is visible from city centres,
 * and a blown-out starfield would contradict the whole glare rule.
 */
import { useMemo } from "react";
import { AdditiveBlending, BufferAttribute, BufferGeometry } from "three";

export function Starfield({ count = 1400 }: { count?: number }) {
  const geometry = useMemo(() => {
    // A small deterministic generator, so the sky never shifts between loads.
    let seed = 20260808;
    const random = () => {
      seed = (seed * 1664525 + 1013904223) % 4294967296;
      return seed / 4294967296;
    };

    const positions = new Float32Array(count * 3);
    const sizes = new Float32Array(count);

    for (let i = 0; i < count; i += 1) {
      // Even distribution over a sphere well outside the camera's reach.
      const u = random() * 2 - 1;
      const theta = random() * Math.PI * 2;
      const r = Math.sqrt(1 - u * u);
      const distance = 120 + random() * 60;
      positions.set([r * Math.cos(theta) * distance, u * distance, r * Math.sin(theta) * distance], i * 3);
      sizes[i] = 0.4 + random() * 1.1;
    }

    const buffer = new BufferGeometry();
    buffer.setAttribute("position", new BufferAttribute(positions, 3));
    buffer.setAttribute("size", new BufferAttribute(sizes, 1));
    return buffer;
  }, [count]);

  return (
    <points geometry={geometry}>
      <pointsMaterial
        color="#CBD6DA"
        size={0.55}
        sizeAttenuation={false}
        transparent
        opacity={0.55}
        blending={AdditiveBlending}
        depthWrite={false}
      />
    </points>
  );
}

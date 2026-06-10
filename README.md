# Schrödinger Equation Integrator

A Python script that numerically solves the time-independent Schrödinger equation for a quantum harmonic oscillator using the Verlet integration method.

## How it works

The script computes the wavefunction ψ(x) by stepping forward with the Numerov/Verlet recurrence:

```
ψ[n+1] = 2·ψ[n] - ψ[n-1] + dx² · f[n] · ψ[n]
```

where `f(x) = (2m/ℏ²)(E - V(x))` and `V(x) = ½mx²` is the harmonic potential.

After integration, the wavefunction is normalized and the probability density |ψ(x)|² is computed. Both are plotted against position.

## Usage

```bash
pip install numpy matplotlib
python integrator.py
```

Parameters like energy `E`, mass `m`, step size `h`, and domain bounds can be adjusted at the top of `integrator.py`.

## Output

Two plots are generated:
- **Wave Function vs Position** — the normalized wavefunction ψ(x)
- **Probability vs Position** — the probability density |ψ(x)|²

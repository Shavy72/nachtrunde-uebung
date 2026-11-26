"""Basis-Tests für die Nachtrunden-Vorlage."""

from uebung.rechner import addieren, verdoppeln


def test_addieren() -> None:
    assert addieren(2, 3) == 5


def test_verdoppeln() -> None:
    assert verdoppeln(4) == 8

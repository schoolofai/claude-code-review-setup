import logging

log = logging.getLogger(__name__)


def list_invoices(conn, page=1, per_page=10):
    """Return one page of invoices, newest first. Pages are 1-indexed."""
    if page < 1:
        raise ValueError("page must be >= 1")
    offset = (page - 1) * per_page
    rows = conn.execute(
        "SELECT id, customer_id, amount_pence FROM invoices ORDER BY id DESC LIMIT ? OFFSET ?",
        (per_page, offset),
    ).fetchall()
    log.info("listed %d invoices (page %d)", len(rows), page)
    return rows

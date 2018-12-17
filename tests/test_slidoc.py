#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `slidoc` package."""

import pytest


from slidoc import slidoc


@pytest.mark.parametrize('bad_targets', ('s5', 123, 'remarkjs'))
def test_value_error(bad_targets):
    with pytest.raises(ValueError,
                       match=str(incorrect) +
                       ' is not one of the 3 supported formats.'):
        make_slides(target=bad_targets)


@pytest.mark.parametrize('not_files', ('not a file', 'this either', 'just no'))
def test_no_file(not_files):
    with pytest.raises(RuntimeError, match='source_file is not a valid path'):
        make_slides(source_file=not_files)


@pytest.mark.parametrize('targets', ('slidy', 'dzslides', 'revealjs'))
def test_doctype(targets):
    """The output should specify the doctype as html"""
    assert "<!DOCTYPE html" in make_slides(target=targets)

@pytest.mark.parametrize('targets', ('slidy', 'dzslides', 'revealjs'))
def test_end_tags(targets):
    """Properly formatted html should end with closing tags"""
    assert make_slides(target=targets).endswith('</body>\n</html>\n')
